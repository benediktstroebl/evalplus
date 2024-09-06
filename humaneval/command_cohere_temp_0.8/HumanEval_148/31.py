```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = None
    p2 = None
    for i, val in enumerate(planets):
        if val == planet1:
            p1 = i
        if val == planet2:
            p2 = i
    if p1 is None or p2 is None:
        return ()
    return (planets[p1:p2+1]).sort()
```

The function `bf` takes two parameters `planet1` and `planet2`, and returns a tuple of all planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. If either of the input planets is not a valid planet name, the function returns an empty tuple.

The code works by first defining a list of all eight planets in the solar system in the `planets` variable. It then iterates through the list, using the `enumerate` function to assign the index of each planet in the list as well as its value. It checks if the value corresponds to either of the input planet names, and if so, stores the index in the variables `p1` or `p2`. After the loop, it checks if either of the `p1` or `p2` variables is `None`, and if so, returns an empty tuple because neither of the input planets is a valid planet name. If neither of the variables is `None`, it returns a slice of the `planets` list from index `p1` to index `p2`, which includes all planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by proximity to the sun, as requested by the prompt.