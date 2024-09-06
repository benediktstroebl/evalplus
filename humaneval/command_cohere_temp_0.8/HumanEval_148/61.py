```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else None
    p2 = planet2.lower() if planet2 in planets else None
    
    if p1 and p2:
        res = []
        for i in range(8):
            if planets[i] == p1 and planets[i] != p2:
                res.append(planets[i])
                res.extend(bf(planets[i], planet2))
                break
            if planets[i] != p1 and planets[i] == p2:
                res.append(planets[i])
                res.extend(bf(planet1, planets[i]))
                break
        return res
    else:
        return ()
```

The provided Python script defines a function called `bf` that performs a breadth-first search to find all planets in the solar system whose orbits are between the orbits of two specified planets, sorted by proximity to the sun. The function takes two planet names as input using the parameters `planet1` and `planet2`. The function first checks if the input planet names are valid and if not, it returns an empty tuple. If the input is valid, it proceeds to recursively explore the solar system, adding relevant planets to the result list. The result is a list of planets sorted by proximity to the sun and limited to those between the orbits of the specified planets.