```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(p1, p2 + 1))
```

The function `bf` takes two strings `planet1` and `planet2` as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first creates a list of all planets. It then finds the indices of `planet1` and `planet2` in the list and checks if they are -1, which indicates that the inputs are not correct planet names. If one of the indices is -1, the function returns an empty tuple. Otherwise, it returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun.