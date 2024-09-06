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

The function first assigns the two planets passed as arguments to two variables `p1` and `p2` with the help of a loop. It assigns `p1` the index of the first occurrence of `planet1` in the `planets` list and `p2` is assigned the index of the first occurrence of `planet2` in the `planets` list. 

If none of the planets are found in the list, it means that the passed values were not correct planet names and the function returns an empty tuple `()`. In any other case, the function returns a tuple containing all planets whose name is located between the planets named `planet1` and `planet2`, sorted by proximity to the sun. The sorting is ensured by the enumeration of the `planets` list, which is sorted by proximity to the sun.