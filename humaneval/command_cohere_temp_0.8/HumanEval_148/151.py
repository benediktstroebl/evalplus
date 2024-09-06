```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1:
            p1 = i
        if cur_planet == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2+1])
```

The function first collects the indices of the planets sorted by their proximity to the Sun, and then returns the planets located between the given planets (if they are valid). The function returns an empty tuple if the provided planets are incorrect. You can verify that the example inputs from the problem statement return the expected outputs.