```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = []
    if p1 and p2:
        for planet in planets:
            if planet == p2 and planet != p1:
                break
            if planet == p1:
                continue
            result.append(planet)
        result.sort(key=lambda x: planets.index(x))
    return tuple(result)
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of all the planets whose orbits are between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. If either of the input planets is not a valid planet name, the function returns an empty tuple. The above code solves the problem with the use of a list of planets and 2 nested loops. The outer loop iterates through the planets with an If-statement that checks if the current planet is the second input planet, if so, the loop breaks to terminate the iteration. If not, the if-statement checks if the current planet is the first input planet, if so, it continues to the next iteration. If not, the inner loop appends the current planet to the result list. The result list is then returned as a tuple after it's sorted by the index of the planet in the planets list.