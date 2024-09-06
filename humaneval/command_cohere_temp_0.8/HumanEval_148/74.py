```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1:
            p1 = i
        if pole == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2+1])
```
The function first collects the indices of the given planets in the list of planets, and then returns the slice of the list between these indices. It also handles the case when an invalid planet name is provided, returning an empty tuple in such cases.