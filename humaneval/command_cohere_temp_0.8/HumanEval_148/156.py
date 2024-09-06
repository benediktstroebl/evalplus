```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p1:p2+1])
``` 

The function first collects the indices of the planets to return a more efficient solution. If one of the planets is incorrect, the function returns an empty tuple. In the worst-case scenario, the function will iterate through all planets, but the majority of the time will be spent searching for planets rather than iterating through the list.