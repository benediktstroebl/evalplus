```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1:
            p1 = i
        if pole == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2+1])
```

The function first tries to find the indices of the given planets in the `planets` list, if either of the indices is -1, it returns an empty tuple `()`, if both indices are found, the function returns a slice of the `planets` list between the two indices, inclusive.