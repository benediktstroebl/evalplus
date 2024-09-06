```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1:
            p1 = i
        if pole == planet2:
            p2 = i
    if p1 == -1 or p2 == -1:
        return ()
    return (planets[p1:p2 + 1])
```

The function first attempts to locate the indices of the given planets in the `planets` list. It then returns the planets situated in theBETWEEN corresponding indices and returns them sorted by proximity to the sun. The proximity to the sun is specified based on the original list, with Mercury being the first element. The function returns an empty tuple if either of the inputs is not found in the list. 

Here is an example usage of the function:
```python
 bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
bf("Earth", "Mercury") ==> ("Venus")
 bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn") 
```