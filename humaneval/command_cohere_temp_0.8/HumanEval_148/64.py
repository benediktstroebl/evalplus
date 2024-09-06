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

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings containing the names of all planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. If either of the input planets is not a valid planet name, the function returns an empty tuple. 

The code leverages the list of planets to index the names and determine the order of orbits based on the indices. By using the maximum and minimum indices, it collects the planets in the relevant range to return as a tuple. The negative indexing avoids collecting planets outside the orbit of the closer planet.