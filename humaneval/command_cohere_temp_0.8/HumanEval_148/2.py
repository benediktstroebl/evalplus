```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return result if result != [] else tuple()
```

The function first collects all planets in the solar system in the `planets` list, and then uses the `index` function to find the position of `planet1` and `planet2`. It then returns all planets in between, sorted by the proximity to the sun, by iterating over the positions and adding them to `result`. The `result` variable is then returned if it's not an empty list, or an empty tuple is returned.