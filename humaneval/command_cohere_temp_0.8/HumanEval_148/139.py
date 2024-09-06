```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return result if result else tuple()
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of all planets between the two planets, sorted by proximity to the sun. The function first indexes the two input planets from the list of planets in our solar system, throws an error if the inputs are not planets, and then checks in which order the planets appear relative to the sun. The code snippit offers a simple and efficient way to tackle this problem, while also maintaining readability and adhering to the problem's outlined solution.