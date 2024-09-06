```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[p1 + 1 : p2])
```

The provided Python script defines a function called `bf` that takes two parameters, `planet1` and `planet2`. This function returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first creates a list of all eight planets and then searches for the indices of `planet1` and `planet2` in this list, ignoring unknown planets. If one or both planets are not found, an empty tuple is returned. Otherwise, the function returns a tuple containing all planets whose orbits are in between, starting from the index after `planet1` up to and including the index before `planet2`. The planets are sorted by their proximity to the sun, ensuring the correct order.