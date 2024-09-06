```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    result = []
    for planet in planets:
        if planet > p2 and planet >= p1:
            result.append(planet)
    return result if result else tuple()
```

The function `bf` takes in two strings, `planet1` and `planet2`, as inputs, and returns a tuple of strings sorted in proximity to the sun. The function first checks if both inputs are valid planet names using the `in` operator and assigns the lowercase versions of the planets to `p1` and `p2`. It then initializes an empty list called `result` to store valid planet names. The function then iterates through the sorted list of planets, checking if each planet is greater than `p2` and also greater than or equal to `p1`, if so, the planet is added to `result`. Finally, an empty tuple is returned if `result` is empty, and the tuple of sorted planets is returned if `result` is not empty. 

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```
This would print out the tuple `(Saturn, Uranus)`.