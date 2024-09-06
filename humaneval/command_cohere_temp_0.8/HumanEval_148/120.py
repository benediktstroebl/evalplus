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

The function `bf` takes two planet names, `planet1` and `planet2`, as strings and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. 

The function first creates a list of all planet names, and then checks if `planet1` and `planet2` are part of this list, and locates their positions in the list. 

If either of the planets is not found in the list, the function returns an empty tuple. Otherwise, it returns a slice of the list from the index of `planet1` to the index of `planet2`, inclusive of the endpoints. The planets in this slice are sorted by their proximity to the sun.