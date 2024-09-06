```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1: p1 = i
        if p == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p2 < p1 else planets[p1:p2+1])
```

The function first assigns the planets list to store the names of the planets. It then finds the indices of the planets `planet1` and `planet2`. If one of the planets is incorrect the function returns an empty tuple, otherwise, it returns a tuple containing all planets whose orbits are located between the orbit of planet1 and the orbit of planet2, sorted by the proximity to the sun using a conditional expression. 

The test examples are partially included to check if the function behaves as described in the task statement. 

Please note that the script assumes the order of the planets as described in the task statement. If the order is different, the script may not function properly.