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

The function first assigns the planets to the `planets` array and then finds the indices `p1` and `p2` of the planets in the array. If the planets are not found, the function returns an empty tuple; otherwise, it returns a tuple of all planets whose index is between `p1` and `p2`, sorted by their proximity to the sun.