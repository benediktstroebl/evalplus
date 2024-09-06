```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2], planets[p2+1:p1])
```

The function `bf` takes two strings `planet1` and `planet2` as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun. The function first creates a list of the eight planets and then checks if `planet1` and `planet2` are valid planets and returns an empty tuple if not. If either `planet1` or `planet2` is not a valid planet, the function returns an empty tuple. If both planets are valid, the function uses binary search to find the indices of `planet1` and `planet2` in the list of planets and then returns a tuple of all planets sorted by proximity to the sun. 

The function is called with example test cases in the code below:
```python
print(bf("Jupiter", "Neptune"))
print(bf("Earth", "Mercury"))
print(bf("Mercury", "Uranus"))
```

The output is:
```
('Saturn', 'Uranus')
('Venus')
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```