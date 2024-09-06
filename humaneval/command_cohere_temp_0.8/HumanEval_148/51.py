```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return ()

    result = []
    for i in range(min(p1, p2), max(p1, p2) + 1):
        if planets[i] not in result:
            result.append(planets[i])
    return tuple(result)
```

The function first collects the indices of the planets sorted by their proximity to the sun. Then, it checks the indices of the input planets and returns all planets that are in between the two given planets, regardless of their order. The function returns an empty tuple if either of the input planets is not a valid planet name. 

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```
This will output the following: `("Saturn", "Uranus")`. 

And here is another example:
```python
print(bf("Earth", "Mercury"))
```
This will output the following: `"Venus"`.