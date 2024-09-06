```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for planet in planets[p1 <= p2]:
        if planet == planet1 or planet == planet2:
            continue
        result.append(planet)
    
    return tuple(result)
```

The function first collects the indices of the planets in the solar system in the `planets` list, and then finds the indices of the given planets `planet1` and `planet2` in the list. In case an incorrect planet name is given, the indices will be -1, and an empty tuple is returned. If the given planets are valid, the function collects all planets in the list whose index is between the indices of `planet1` and `planet2`, and adds them to the `result` list. The `result` list is returned as a tuple.