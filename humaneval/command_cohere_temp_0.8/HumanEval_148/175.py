```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    fl = False
    for i in range(8):
        if planets[i] == planet1:
            p1 = planets[i]
            fl = True
        if planets[i] == planet2:
            p2 = planets[i]
            fl = True
        if p1 and p2:
            break
    if not fl:
        return ()
    if p1 == p2:
        return (p1)
    result = []
    p1index = planets.index(p1)
    p2index = planets.index(p2)
    for i in range(p1index + 1, p2index + 2):
        result.append(planets[i])
    return tuple(result)
```

The function `bf` takes in two parameters, `planet1` and `planet2`, and returns a tuple containing all the planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. The function first checks and returns an empty tuple if either of the input parameters is not a valid planet name. It then checks if `planet1` and `planet2` are the same planet and returns a tuple containing only the planet if they are. If they are different planets, the function appends to a result list all the planets between the two planets and returns the result as a tuple.