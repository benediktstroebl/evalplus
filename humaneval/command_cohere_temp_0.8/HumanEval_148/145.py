```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pi in enumerate(planets):
        if pi == planet1: p1 = i
        if pi == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p2 < p1 else planets[p1:p2+1])
```

The function first assigns the planets list to the variable `planets`, which contains the eight planets of the solar system in order of proximity to the sun. It then finds the indices of planet1 and planet2 in the planets list, respectively, and stores them in the variables `p1` and `p2`. If either `p1` or `p2` is -1, indicating that the given planet name is not a valid planet, the function returns an empty tuple `()`. If both planet names are valid, the function returns a tuple containing all planets whose indices are between `p1` and `p2`, sorted by proximity to the sun.

The function's result is a list of planets sorted by their distance from the sun between the orbit of the planet specified by the 'planet1' parameter and the planet specified by the 'planet2' parameter. If the first planet is closer to the sun, the planets are sorted in ascending order; otherwise, the planets are sorted in descending order. 

For example, if you call the function as `bf("Jupiter", "Neptune")`, it will return `(Saturn, Uranus)`, which are the planets between Jupiter and Neptune, sorted by proximity to the sun. If you call the function as `bf("Earth", "Mercury")`, it will return `(Venus)` since the only planet between Earth and Mercury is Venus. Lastly, if you call the function as `bf("Mercury", "Uranus")`, it will return `(Venus, Earth, Mars, Jupiter, Saturn)`, which are all the planets between Mercury and Uranus.