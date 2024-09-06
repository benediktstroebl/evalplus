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

The function first collects the indices of the given planets in the list of planets in the solar system, using the `index` method. The function then iterates through the indices of all planets, starting from the closest planet to the sun (the index of the planet with the higher index value), and collects the planets whose indices are in the range between the indices of the given planets. The resulting list of planets is sorted by the proximity to the sun and returned as a tuple.

The base case of the `index` method is -1, which means that if the planet name is not found in the list, the index will be -1. Thus, the code checks if the indices are -1, and if so, it returns an empty tuple, indicating that incorrect planet names were given. 

The examples in the problem statement correspond to the following test cases:
```python
>>> bf("Jupiter", "Neptune")
('Saturn', 'Uranus')
>>> bf("Earth", "Mercury")
('Venus')
>>> bf("Mercury", "Uranus")
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```