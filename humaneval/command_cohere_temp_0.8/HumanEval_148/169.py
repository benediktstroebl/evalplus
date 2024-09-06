```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(min(p1, p2), max(p1, p2) + 1):
        if planets[i] not in result:
            result.append(planets[i])
    
    return tuple(result)
```

The function first collects the indices of the planets sorted by their proximity to the sun. If the provided planets are not in the list of planets, the function returns an empty tuple. Otherwise, it collects all planets within the range of indices of the provided planets and returns them sorted by their proximity to the sun.