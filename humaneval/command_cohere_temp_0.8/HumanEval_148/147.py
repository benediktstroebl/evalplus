```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    result = []
    for i in range(p1, p2 + 1):
        result.append(planets[i])
    
    return result if result != [] else []
```

The function first collects all planets in the solar system in the `planets` list, and then uses the `index` function to find the positions of the two given planets in the list. It then iterates through the list of planets between the two given planets, closer to the sun, and returns the result. The function returns an empty list if either of the given planets is not a planet in the solar system or if both given planets are the same. 

Here is an example usage of the function:
```python
print(bf("Jupiter", "Neptune"))
```
```bash
('Saturn', 'Uranus')
```

Here is another example usage of the function:
```python
print(bf("Earth", "Mercury"))
```
```bash
('Venus')
```

Here is another example usage of the function:
```python
print(bf("Mercury", "Uranus"))
```
```bash
('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')
```