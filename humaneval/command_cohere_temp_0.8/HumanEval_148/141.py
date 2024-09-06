```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(max(p1, p2), min(p1, p2), -1):
        if i >= 0 and i < len(planets):
            result.append(planets[i])
    
    return tuple(result)
```

The function `bf` takes in two strings, `planet1` and `planet2`, and returns a tuple of strings of all planets between the two planets, sorted by their proximity to the sun. The function first finds the indices of `planet1` and `planet2` in the list of planets and then uses a list comprehension to find all the planets between the two planets, given by their indices. The list comprehension goes from the index of the closer planet to the index of the farther planet in reverse order, so that the planets are sorted by their proximity to the sun. 

The function then returns a tuple of the sorted planet names. If either of the input planets is not a correct planet name, the function returns an empty tuple. 

Here is an example of using the function:
```python
 bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
```

And here is another example:
```python
 bf("Earth", "Mercury") ==> ("Venus")
```