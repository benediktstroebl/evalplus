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

The function first collects all planets in the solar system in the `planets` list, and uses the `index` function to find the indices of the planets' location relative to Mercury in the `p1` and `p2` variables. The function then checks if the inputted planets are valid, and if so, loops through the planets in descending order to collect all planets between the two inputted planets, and returns the result as a tuple. The descending order is essential as it ensures that the output tuple has planets sorted by their proximity to the sun. 

The test cases are:
```python
test_bf = {
    ("Jupiter", "Neptune"), ("Saturn", "Uranus"): ("Saturn", "Uranus"),
    ("Earth", "Mercury"), ("Venus"): ("Venus"),
    ("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"): ("Venus", "Earth", "Mars", "Jupiter", "Saturn"),
}
```