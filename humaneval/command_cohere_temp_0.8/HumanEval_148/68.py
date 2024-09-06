```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return ()

    return tuple(planets[p1:p2+1])
```

The function `bf` takes two planet names, `planet1` and `planet2`, as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first creates a list of all planets and uses the `index` function to sort them by proximity to the sun. It then uses these indices to create a slice for the planets whose orbits are between the given planets. Lastly, it returns a tuple of these planets.