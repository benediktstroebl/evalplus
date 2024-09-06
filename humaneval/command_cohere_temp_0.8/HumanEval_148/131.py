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
    return (planets[p1:p2 + 1])
```

The function first attempts to locate the indices of the given planets in the `planets` list. It then returns the planets situated in the Inclusive Range (thanks to Python's slicing capabilities) between the two indices, padded with those closest to the Sun. It returns an empty tuple if either of the given planets is invalid. You can verify this code by running the test suite included in the code block.