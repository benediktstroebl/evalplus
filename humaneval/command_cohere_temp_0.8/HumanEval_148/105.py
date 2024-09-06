```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1: p1 = i
        if p == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p2 < p1 else planets[p1:p2+1])
```

The function first collects the indices of `planet1` and `planet2` in the list of planets. If any of the planets is not found in the list, the function returns an empty tuple. Otherwise, it returns a tuple of planets whose indices are between `planet1` and `planet2`, sorted by their proximity to the sun.