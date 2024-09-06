```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[(p2 + 1) % 8], planets[((p1 - 1) + 8) % 8])
```
The problem is solved using a list of planets and two variables to store the indices of the planets relative to the sun. These indices are used to determine the relative positions of the planets and return the correct sequence of planets. In the case where an invalid planet is entered, the function returns an empty tuple. This is checked for using the if condition and the p1 and p2 variables.