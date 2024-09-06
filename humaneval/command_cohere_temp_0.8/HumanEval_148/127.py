```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = [p for p in planets if p1 <= p <= p2]
    return result if result else ()
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings containing the planets whose orbits are located between the orbit of `planet1` and `planet2`, sorted by proximity to the sun. The function first creates a list of the eight planets, then checks if `planet1` and `planet2` are valid with the `in` operator. If neither or either of these is valid, it defaults the variables to an empty string. It then uses a list comprehension to populate `result` with all planets between the two valid planets going by their alphabetical order, as well as sorting them by proximity to the sun. 

The result is then returned if it is not an empty list; otherwise, an empty tuple is returned. You can test this function by calling it with two different combinations of valid planet names and invalid names to see if it returns the correct output. 

Please note that the code assumes a valid sorting of planets by their proximity to the sun, which is not specified in the prompt. You can adjust the code to your liking if you wish to sort the planets in a different order.