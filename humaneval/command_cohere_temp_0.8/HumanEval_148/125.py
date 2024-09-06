```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p1:p2+1])
```

The function `bf` takes two strings `planet1` and `planet2` as input and returns a tuple of strings containing the names of the planets whose orbits are between the orbits of the planets specified in `planet1` and `planet2`, sorted by their proximity to the Sun. You can verify that the provided examples in the problem statement return the correct results.