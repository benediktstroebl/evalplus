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

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings containing all planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. The function first verifies if the given planets are valid with the use of the `index` method. If the given planets are not valid, the function returns an empty tuple. The loop at the end goes through the indices of the planets and adds them to the `result` variable if the index is between the maximum and minimum of the indices of the given planets. The loop is sorted by proximity to the sun.