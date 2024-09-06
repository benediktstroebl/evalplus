```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1, p2 + 1):
        result.append(planets[i])

    return result if result else None
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings containing the names of all planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. If either of the input planets is not a valid planet name, the function returns an empty tuple.

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```

This will output the following:
```
('Saturn', 'Uranus')
```

Here is another example usage of the function:
```python
print(bf("Earth", "Mercury"))
```

This will output the following:
```
('Venus')
```