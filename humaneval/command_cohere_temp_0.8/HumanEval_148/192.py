```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    return tuple(planets[p1:p2+1])
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of the planets between the two input planets in terms of their distance from the sun. The function first creates a list of the eight planets, and uses the `index` function to find the indices of the two input planets in the list. If either of the inputs is not a planet, then both indices will be -1, and the function will return an empty tuple `()`. If both indices are valid, the function returns a tuple of the planets in that orbit, with a start index of `p1` and an end index of `p2`, inclusive. The return value is sorted by the proximity to the sun.