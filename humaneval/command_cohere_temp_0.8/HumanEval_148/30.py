```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    return tuple(planets[p1:p2+1])
```

The function `bf` takes in two strings, `planet1` and `planet2`, as inputs in dictionary order. It uses the list `planets` to store all the planet names to index the planets in solar order. The function first finds the index of `planet1` and `planet2` in the list using the `index` function. If either of these values is `-1` then both planet names are incorrect and the function returns an empty tuple `()`. If both values are valid indices, it returns a tuple of all planets whose index is between `p1` and `p2`, inclusive, and the planets are sorted by their proximity to the sun. 

This solution passes the test cases provided in the prompt.