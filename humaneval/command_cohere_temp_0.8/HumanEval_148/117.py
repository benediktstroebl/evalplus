```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pi in enumerate(planets):
        if pi == planet1: p1 = i
        if pi == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(p1, p2 + 1))
```

The function `bf` takes two strings `planet1` and `planet2` as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by proximity to the sun. The function first creates a list of the eight planets and then checks if `planet1` and `planet2` are valid planets and returns an empty tuple if not. If they are valid planets, the function determines the indices of `planet1` and `planet2` in the list of planets and uses the indices to slice the list and returns a tuple of the planets located between the two.