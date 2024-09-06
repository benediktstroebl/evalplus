```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(min(p1, p2) + 1, max(p1, p2) + 2))
```

The function first collects the indices of `planet1` and `planet2` in the `planets` list and checks if they are -1, and if so, returns an empty tuple. Otherwise, it returns a tuple with all planets whose indices are between the ones of `planet1` and `planet2`, inclusive, except for the planets that are equal to `planet1` and `planet2`.