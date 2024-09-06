```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for planet in planets[p1 <= p2]:
        if planet == planet1:
            continue
        if planet == planet2:
            break
        result.append(planet)
    
    return tuple(result)
```

The function first collects the indices of the planets in the solar system in the `planets` list, and then finds the indices `p1` and `p2` of the given planets in the list. 

The subsequent looping through the planets in the list compares each planet's index to `p2` and `p1` respectively. If the planet's index is smaller than `p2`, it means the planet is closer to the sun than `planet2`, and if the planet's index is greater than `p1`, the planet is farther away from the sun than `planet1`. Thus, the function only adds to the `result` list the planets which are located between the orbits of `planet1` and `planet2` from the sun, and returns the list as a tuple.