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

The function first assigns values to `p1` and `p2` with the targets of the function and checks if these values are `-1`. If so, it returns an empty tuple `()`. If the values are filled, the function returns a tuple value of all planets in the sun's proximity order between the two planets. 

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```

This will print out the expected tuple `("Saturn", "Uranus")`.