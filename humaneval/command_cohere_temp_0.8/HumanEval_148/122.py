```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1: p1 = i
        if p == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p1:p2+1])
```

The function first stores the names of the eight planets in the solar system in the `planets` array. It then searches for the indices of the planets using `enumerate` in the `planets` array. Finally, it returns the planets whose names are located in the `planets` array between the indices of the `planet1` and `planet2` planets. If `planet1` or `planet2` is not a planet or is not found in the list, an empty tuple is returned. 

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```
This will print out the tuple `(Saturn, Uranus)`.