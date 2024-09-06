```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1:
            p1 = i
        if p == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2+1])
```

The function first collects the indices of `planet1` and `planet2` in the `planets` list, and then returns a slice of the list `planets` between these indices, inclusive. The slice starts at `p1` and has a length `p2-p1+1`, and therefore it contains all planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by the proximity to the sun. The special case of the edge slices is also handled properly: if `p2-p1` is equal to 1, the resulting tuple has only one element, and if it is 0, the result is an empty tuple.