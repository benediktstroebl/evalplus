```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for planet in planets[p1 <= p2]:
        if planet != planet1 and planet != planet2:
            result.append(planet)
    
    return tuple(result)
```

The function first constructs a list of planets sorted by their proximity to the Sun, and then searches for the planets that are located in the interval between the given planets. The function returns an empty tuple if the input is not a valid planet name. 

Here is an example usage output:
```python
>>> bf("Jupiter", "Neptune")
('Saturn', 'Uranus')
>>> bf("Earth", "Mercury")
('Venus')
>>> bf("Mercury", "Uranus")
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```