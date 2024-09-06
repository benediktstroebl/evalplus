```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for planet in planets[p1 <= p2]:
        if planet != planet1 and planet != planet2:
            result.append(planet)
    
    return tuple(result)
```

The function first collects the indices of the planets in the solar system in the `planets` list, then it finds the indices of the given planets `planet1` and `planet2` in the list using the `index` function. If either of the indices is -1, indicating that the planet is not listed in the solar system or not given, an empty tuple is returned. If both indices are found, the function adds to the `result` list all the planets from the `planets` list between the two indices, ignoring `planet1` and `planet2`. The resulting list is returned as a tuple.