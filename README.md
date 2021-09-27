# Python Live Project
 My contribution to a Django site for managing collections. This section allows users to collect and review music albums. It also fetches a current list of top albums using Beautiful Soup.

![image](https://user-images.githubusercontent.com/84836870/134848852-a975f2f4-2978-4777-b427-684e1e61130c.png)

From views.py:
```python
def AlbumReviews_home(request):
    source = requests.get('https://www.officialcharts.com/charts/albums-chart/').text
    soup = BeautifulSoup(source, features='html.parser')
    chart = soup.find('table', class_='chart-positions')
    albums = []

    for album in chart.find_all('div', class_='track', limit=10):
        cover_src = album.find('img')['src']
        title = album.find('div', class_='title').a.text
        artist = album.find('div', class_='artist').a.text
        album = (cover_src, title, artist)
        albums.append(album)

    context = {'albums': albums}

    return render(request, "AlbumReviews/AlbumReviews_home.html", context)
```

![image](https://user-images.githubusercontent.com/84836870/134848937-8feaa46b-b4df-4aa1-bdf0-86cfa971bf6f.png)

From models.py:
```python
class Album(models.Model):
    Name = models.CharField(max_length=50, null=False, blank=False)
    Artist = models.CharField(max_length=30, null=False, blank=False)
    Year = models.IntegerField(default=2021)
    Genre = models.CharField(max_length=50)
    Rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    Review = models.TextField(default="Type your review here (optional)")

    objects = models.Manager()
```

From urls.py:
```python
urlpatterns = [
    path('', views.AlbumReviews_home, name="AlbumReviews_home"),
    path('add/', views.AlbumReviews_add, name="AlbumReviews_add"),
    path('list/', views.AlbumReviews_list, name="AlbumReviews_list"),
    path('details/<int:id>', views.Album_details, name="AlbumReviews_details"),
    path('delete/<int:id>', views.Album_delete, name='AlbumReviews_delete'),
    path('edit/<int:id>', views.Album_edit, name='AlbumReviews_edit'),
]
```

From AlbumReviews_details.html:
```python
{% extends 'AlbumReviews/AlbumReviews_base.html' %}
	{% block title%}{{ details.Name }} &#8212; {{ details.Artist }}{% endblock %}

	{% block content %}
		<div>
      <div class="album_list">
          <h1>
              {% filter upper %}
                  {{ details.Name }} &#8212; {{ details.Artist }}
              {% endfilter %}
          </h1>
          <div class="album">
              <div class="info">
                  <span class="album_details"><h3>Year:</h3> {{ details.Year }}</span>
                  <span class="album_details"><h3>Genre:</h3> {{ details.Genre }}</span>
                  <span class="album_details"><h3>Rating:</h3> {{ details.Rating }}</span>
                  <a href="{% url 'AlbumReviews_edit' details.id %}"><button>Edit</button></a>
                  <a href="{% url 'AlbumReviews_delete' details.id %}"><button>Delete</button></a>
              </div>
              <p>{{ details.Review }}</p>
          </div>
      </div>
		</div>
	{% endblock %}
```
