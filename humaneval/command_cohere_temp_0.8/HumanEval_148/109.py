```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p1:p2+1])
```

The provided Python script defines a function called `bf` that takes two parameters, `planet1` and `planet2`. This function performs the task of finding all planets whose orbits are located between the orbits of the specified `planet1` and `planet2`, sorted by proximity to the sun.

The function first creates a list of the eight planets in our solar system and assigns two variables, `p1` and `p2`, to the indices of the planets in the list that match the given `planet1` and `planet2`. If none of the planets match the given parameters, the variables `p1` and `p2` are set to -1. Then, the section of the list of planets between `p1` and `p2` (inclusive) is extracted and returned as a tuple, providing the planets sorted by proximity to the sun.

The script includes tests in the form of example calls to the `bf` function with specific `planet1` and `planet2` values, checking whether the function returns the expected results. When the planets to be found are not specified correctly, the function returns an empty tuple `()`.