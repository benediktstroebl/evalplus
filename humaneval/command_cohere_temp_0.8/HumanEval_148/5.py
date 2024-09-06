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

The function first assigns the two planets passed as parameters to two variables `p1` and `p2` with `enumerate`, and then through these variables checks if the planets are valid. If one (or both) is not valid, it returns an empty tuple `()`. If the planets are valid, it returns a sorted tuple of planets whose indexes are between `p1` and `p2` (inclusive for the lower bound, exclusive for the upper bound).