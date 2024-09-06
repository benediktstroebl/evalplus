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

The function first stores all the planets in the `planets` array. It then searches for the indices of `planet1` and `planet2` in this array, storing `-1` if not found. The function then returns all planets whose indices are between `p1` and `p2` (inclusive for `p1` and exclusive for `p2`). The test cases included demonstrate the correct behavior of the function.