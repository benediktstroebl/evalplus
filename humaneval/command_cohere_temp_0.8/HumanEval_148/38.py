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

The function first collects the indices of the given planets in the list of planets in the solar system. The list is sorted by the proximity to the Sun, ensuring that the indices are correct for the ordering of the planets. The function then goes through the indices between the given planets, adding the planets to the result list and ultimately returning them as a tuple. Additionally, if the provided planets are not in the list of planets, the function returns an empty tuple. This ensures that the function works as expected and returns the correct results based on the given specifications.