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

The function first stores all the planets in the `planets` array. It then finds the indices of `planet1` and `planet2` in the array. If either of the planets is not found (`-1`), it returns an empty tuple. Otherwise, it returns a tuple of all planets whose indices are between `p1` and `p2`, inclusive, and sorted by their indices, which corresponds to their proximity to the sun in the given order.