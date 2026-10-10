

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# Достаём координаты в отдельные переменные
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# Moscow <-> London
distances['Moscow'] = {}
distances['Moscow']['London'] = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5

# Moscow <-> Paris
distances['Moscow']['Paris'] = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5

# London <-> Moscow
distances['London'] = {}
distances['London']['Moscow'] = ((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** 0.5

# London <-> Paris
distances['London']['Paris'] = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

# Paris <-> Moscow
distances['Paris'] = {}
distances['Paris']['Moscow'] = ((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** 0.5

# Paris <-> London
distances['Paris']['London'] = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** 0.5

print(distances)

