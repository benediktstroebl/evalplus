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
    return tuple(planets[p1 + 1 : p2])
```
The function first collects the indices of the given planets in the list of planets, and then sequentially checks these indices. If one of the given planets is not found in the list, the function returns an empty tuple. Otherwise, it returns a tuple of all planets located between the two given planets, starting with the planet closer to the sun. The output is sorted by the proximity to the sun.