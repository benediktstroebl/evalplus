```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    for p in range(8):
        if planets[p] == planet1:
            p1 = p
        if planets[p] == planet2:
            p2 = p
    if p1 is None or p2 is None:
        return ()
    return tuple(planets[p] for p in range(max(p1, p2) + 1, min(p1, p2), -1))
```

The function `bf` takes two planet names, `planet1` and `planet2`, as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by their proximity to the sun. The function first creates a list of the eight planets and then checks if `planet1` and `planet2` are valid planet names. If either of them is not a valid planet name, the function returns an empty tuple. If both planet names are valid, the function uses binary search to find the indices of `planet1` and `planet2` in the list of planets and then returns all planets sorted by their proximity to the sun, from the index of `planet2` down to the index of `planet1`, inclusive.