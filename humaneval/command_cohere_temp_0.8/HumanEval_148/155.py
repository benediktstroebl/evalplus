```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])
    
    return result if result != [] else None
```

The function first collects all planets in the solar system in the `planets` list, and then uses the `index` function to find the position of `planet1` and `planet2`. It then iterates through the positions in between these two and adds the corresponding planet name to the `result` list. The function returns an empty tuple `()` if either `planet1` or `planet2` is not a valid planet name. You can test the function by calling it with different combinations of `planet1` and `planet2` arguments.