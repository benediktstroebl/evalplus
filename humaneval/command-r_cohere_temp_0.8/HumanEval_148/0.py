```python
def bf(planet1, planet2):
    '''
    Returns a tuple containing planets with orbits between planet1 and planet2.
    '''
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    planet1_index = planets.index(planet1)
    planet2_index = planets.index(planet2)
    
    if planet1_index or planet2_index == -1:
        return ()

    left = planet1_index
    right = planet2_index

    result = []
    for planet in planets[left:right+1]:
        result.append(planet)

    return tuple(sorted(result, key=planets.index))
```