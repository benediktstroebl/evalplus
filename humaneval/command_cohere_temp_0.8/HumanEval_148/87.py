```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    return tuple(planets[p1:p2+1])
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings containing the names of all planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. If either of the input planets is not a valid planet name, the function returns an empty tuple. 

The code achieves this by utilizing the list `planets`, which contains the names of the eight planets, and utilizes `index` to find the indices `p1` and `p2` of the planets `planet1` and `planet2` respectively. If either index is `-1` (signifying that the planet name is invalid), it returns an empty tuple `()`. It then slices the `planets` list from index `p1` to `p2` (exclusive), packs the resulting sublist into a tuple, and returns it.