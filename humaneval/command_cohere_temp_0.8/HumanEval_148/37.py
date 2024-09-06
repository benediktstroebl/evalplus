```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return ()

    return tuple(planets[p1:p2+1])
```

The function `bf` takes two planet names, `planet1` and `planet2`, as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first constructs a list of the eight planets, then uses the list's built-in `index` function to find the indices of `planet1` and `planet2`. If either of these indices is -1, meaning that the planet is not among the eight planets, the function returns an empty tuple `()`. Otherwise, the function returns a tuple containing the planets in the range of indices from `planet1` to `planet2` inclusive, sorted by the proximity to the sun.