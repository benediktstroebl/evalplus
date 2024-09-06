```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    return tuple(planets[p1:p2+1])
```

The function `bf` takes in two parameters, `planet1` and `planet2`, and returns a tuple of all the planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. The function first creates a list of the eight planets, and then uses the list's `index` method to find the indices of `planet1` and `planet2`. The code then checks if the indices are invalid, in which case it returns an empty tuple. Otherwise, it returns a tuple of the planets sorted by proximity to the sun.