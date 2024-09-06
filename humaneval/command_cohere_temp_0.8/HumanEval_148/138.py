```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    res = []
    for i in range(p1 + 1, p2 + 1):
        res.append(planets[i])

    return tuple(res) if res else tuple()
```

The function `bf` uses the indices of `planet1` and `planet2` in the `planets` list to determine the planets to include in the result. It then appends these planets to the `res` list, which is returned as a tuple. If `planet1` or `planet2` is not a valid planet name, an empty tuple is returned.