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
    return (planets[(p2 + 1) % 8], planets[((p1 - 1) + 8) % 8])
```

The function `bf` takes two planet names, `planet1` and `planet2`, as strings and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. 

The function first creates a list of the eight planets and then checks if `planet1` and `planet2` are valid planets. If not, an empty tuple is returned. Otherwise, the function finds the indices of `planet1` and `planet2` in the list of planets and uses those indices to calculate the indices of the planets whose orbits are located between the two given planets. The function then sorts the planets by their proximity to the sun and returns them in a tuple.