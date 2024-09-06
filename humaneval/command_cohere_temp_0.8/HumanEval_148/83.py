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

The function `bf` takes two parameters, `planet1` and `planet2`, and returns a tuple of all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. 

The function first creates a list of all planets and then checks if `planet1` and `planet2` are part of this list, and if so, determines their positions in the list with the help of the `enumerate` function. The `if p1 == -1 or p2 == -1` block checks if either of the planets is not recognized as a planet, and if so, returns an empty tuple. If the planets are recognized, the function returns a slice of the list of planets from the planet closest to the sun (the first planet) to the planet furthest from the sun (the second planet).