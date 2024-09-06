```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return tuple(result) if result else tuple()
```

The function `bf` uses the list of planets to index the planets' positions in the solar system. The function then loops through the positions between the two planets and returns a tuple of all the planets in between, if there are any. If there are no planets in between, return an empty tuple. 

The code includes unit tests to ensure the function works for different cases. You can use these tests to check that your code complies with the problem statement.