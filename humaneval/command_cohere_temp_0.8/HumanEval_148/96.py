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

The function first collects the indices of the given planets in the array of planets. If the given planets are not correct, the function returns an empty tuple. If the given planets are correct, the function collects all planets located in orbits between the two given planets, sorts them ascendingly, and returns the resulting tuple. 

The test cases cover the following scenarios:
- `bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")`
- `bf("Earth", "Mercury") ==> ("Venus")`
- `bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")`