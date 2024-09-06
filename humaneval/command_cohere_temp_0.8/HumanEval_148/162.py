```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1:
            p1 = i
        if p == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1 <= p2][p1:p2+1])
```

The function first collects the indices of `planet1` and `planet2` in the `planets` list, and then checks if the index is -1, which indicates that the planet name is incorrect. If the planet name is correct, it returns a tuple of correct planets located in the orbit of `planet1` to the orbit of `planet2`, sorted by their proximity to the sun.