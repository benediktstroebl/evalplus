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

The function first stores all the planets in the `planets` array. It then tries to find the indices of the planets in the array with the planet names given in the parameters. If one of the planets is not found in the array or both are found, the function returns an empty tuple `()` or a sliced sequence of planets respectively. 

The resulting code creates a function that solves the task explained in the prompt and fulfills the conditions listed in the comment.