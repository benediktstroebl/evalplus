```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(max(p1, p2), min(p1, p2) - 1, -1):
        if planets[i] not in result:
            result.append(planets[i])
    
    return tuple(result)
```

The function first collects the indices of the planets in the `planets` list, denoting the order of planets in proximity to the Sun. Then, it uses integer indexing to find the indices of the `planet1` and `planet2` in the list. If either of the input planets is not a valid planet name, both indices will be -1, resulting in an empty tuple being returned. Finally, it loops through the indices from the largest to the smallest, adding each planet to the `result` list if it hasn't been added yet, considering the sorting by the proximity to the Sun. The final result is returned as a tuple.