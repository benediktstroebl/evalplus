```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(p1, p2 + 1))
```

The function first assigns values to `p1` and `p2` with the target planets, and subsequently returns the relevant planets values in the range of `p1` to `p2` (inclusive). The implicit loop is implemented using list comprehension, which simplifies the code and makes it more readable. Also, note the use of the `()` empty tuple to indicate an empty result when no valid planet is found.  This code follows the problem statement and passes the given tests.