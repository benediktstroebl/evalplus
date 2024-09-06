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

The function `bf` uses the list of planets to create two indices: `p1` for the position of the first planet and `p2` for the position of the second planet. It then checks if these indices are valid references to avoid exceptions. Using the maximum and minimum values of these indices, it steps through the list in reverse to collect all planets between the two referenced planets, handling cases where the planets are out of order. The function returns a tuple of sorted names of the planets.