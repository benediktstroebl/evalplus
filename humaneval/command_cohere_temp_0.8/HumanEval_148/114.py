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
    return (planets[p1:p2+1])
```

The function first collects the indices of the planets planet1 and planet2 in the planets list. If none of the planets is found, the function returns an empty tuple. Otherwise, it returns a tuple of all planets whose indices are in the range of the closest planet to the sun to the furthest planet from the sun.