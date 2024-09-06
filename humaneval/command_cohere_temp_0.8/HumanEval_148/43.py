```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for planet in planets[p1 <= p2]:
        if planet == planet1:
            continue
        if planet == planet2:
            break
        result.append(planet)
    
    return tuple(result)
```

The function first collects the indices of the planets in the solar system in the `planets` list, and then finds the indices `p1` and `p2` of the given planets in the list. 

The subsequent loop goes through the planets between these indices, excluding `planet1` and stopping at `planet2`. The resulting list of planets is returned as a tuple.