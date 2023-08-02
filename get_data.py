import requests
import math

def get_movies(id, page_num):
    url = f"https://backend.cineasterna.com/library/title/get_titles?library_id={id}&country_iso=se&page={page_num}&locale=sv&sort=asc&genres=%5B%5D&languages=%5B%5D&years=%5B%5D&ratings=%5B%5D&portal_sessionid=5c64452cfb404cf8b60a5ea2aa458da7"

    response = requests.get(url)
    response = response.json()

    return response

get_all_libraries_url = "https://backend.cineasterna.com/library/library/get_all_libraries?country=se&portal_sessionid=5c64452cfb404cf8b60a5ea2aa458da7"

all_libraries = requests.get(get_all_libraries_url)
all_libraries = all_libraries.json()

movie_list = []

for library in all_libraries["libraries"]:
    page_num = 1

    print(f"library id: {library['id']}")

    response = get_movies(library["id"], 1)
    total_pages = math.ceil(response["count"] / 28)

    movie_list.extend(response["titles"])

    page_num += 1

    while True:
        movies = get_movies(library["id"], page_num)

        movie_list.extend(movies["titles"])

        if page_num == total_pages:
            break
        else:
            page_num += 1


duplicate_movies = set()

unique_list = []

for obj in movie_list:
    if obj["id"] not in duplicate_movies:
        unique_list.append(obj)
        duplicate_movies.add(obj["id"])

print(unique_list)
print(len(unique_list))