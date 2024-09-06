```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pi in enumerate(planets):
        if pi == planet1: p1 = i
        if pi == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p2 < p1 else planets[p1:p2+1])
```

The function first stores the planets in the `planets` array. It then parses the array to locate the indices of `planet1` and `planet2`, assigning them to `p1` and `p2` respectively. If either `p1` or `p2` is -1, the function returns an empty tuple `()`. If neither is the case, the function returns all planets between the two indices, sorted by proximity to the sun.