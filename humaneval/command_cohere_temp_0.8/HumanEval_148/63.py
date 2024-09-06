```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(max(p1, p2), min(p1, p2), -1):
        if i >= 0 and i < len(planets):
            result.append(planets[i])
    
    return tuple(result)
```

The function first collects the indices of the given planets in the array of planets. If the given planets are not found in the array, the function returns an empty tuple. In all other cases, it loops through the array of planets in the reversed order, collecting all planets located between the two given planets, and returns them as a tuple. The sorting is achieved due to the fact that the array of planets is sorted by the proximity to the sun.