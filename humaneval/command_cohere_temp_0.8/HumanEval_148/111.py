```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1: p1 = i
        if p == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(p1, p2 + 1))
```

The function first collects all the planets in a list `planets` and then tries to find the indices `p1` and `p2` of the given planets in the list. If one of the planets is not found in the list, it returns an empty tuple `()`. If both planets are found, it returns a tuple of all planets whose index is between `p1` and `p2` sorted by the proximity to the sun.