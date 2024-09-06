```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(min(p1, p2), max(p1, p2) + 1):
        if i in (p1, p2):
            continue
        result.append(planets[i])
    
    return tuple(result)
```

The function first collects all relevant planets into the `result` list. Then, it returns this list wrapped into a tuple to comply with the problem statement requirements. This solution is linear in the size of the result, which is a good characteristic for this problem. It also avoids unnecessary sorting by iterating through the planets in order and avoiding duplicate entries.