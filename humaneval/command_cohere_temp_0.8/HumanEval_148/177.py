```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, p in enumerate(planets):
        if p == planet1:
            p1 = i
        if p == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2+1])
```

The function first collects the indices of `planet1` and `planet2` in the `planets` list, and then returns a slice of the list between these indices. To pass the test cases, the function handles incorrect planet names correctly by returning an empty tuple. You can easily modify the script to add more test cases.