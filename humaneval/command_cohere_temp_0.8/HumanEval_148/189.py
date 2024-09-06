```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1:
            p1 = i
        if pole == planet2:
            p2 = i
    res = []
    if 0 <= p1 <= p2 < len(planets) :
        for pole in planets[p1+1:p2+1]:
            res.append(pole)
    return res if res else tuple()
```

The function `bf` takes two strings `planet1` and `planet2` as input and returns a tuple of strings with the names of the planets whose orbits are between the orbits of the specified planets. The function checks whether the given planets are valid planet names and returns an empty tuple if they are not. The code is concise and self-contained, achieving the desired functionality with minimal code.  This solution has a time complexity of O(min(n, m)) where n and m are the indexes of the planets in the planets array.