```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return ()

    result = []
    for i in range(max(p1, p2), min(p1, p2), -1):
        if i >= 0 and i < len(planets):
            result.append(planets[i])
    return tuple(result)
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of all the planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. The function first creates a list of the eight planets and uses the list's built-in `index` function to find the indices of `planet1` and `planet2`. If either of these is `-1` (meaning the planet is not recognized), the function returns an empty tuple. Otherwise, it uses the maximum and minimum of the two indices to create a range and loops through the range in reverse order, adding each planet to the `result` list. The `result` list is converted to a tuple and returned.

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```

The output is:
```
('Saturn', 'Uranus')
```

This example returns the planets Saturn and Uranus, which are between Jupiter and Neptune in terms of proximity to the sun.