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

The function first collects the indices of the planets in the solar system in the `planets` list, then it retrieves the indices of the given planets `planet1` and `planet2` using the `index` method. It then sorts the indices and retrieves the planets accordingly, taking into account the descending order and whether the planet exists or not, resulting in a valid solar system order. 

The resulting planets are then appended to a list and returned as a tuple.