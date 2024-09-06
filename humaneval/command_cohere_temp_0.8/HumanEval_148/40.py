```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)
    
    if p1 == -1 or p2 == -1:
        return ()
    
    result = []
    for i in range(max(p1, p2), min(p1, p2) - 1, -1):
        if planets[i] not in result:
            result.append(planets[i])
    
    return tuple(result)
```

The function first collects the indices of the planets using the `planets` list, and then checks if the inputted planets are valid using `p1` and `p2` indices. With the maximum and minimum values of these indices, it iterates through the list to collect all planets within the correct range and returns the result as a tuple. 

The test examples are included within the script:
```python
test_bf = {
    ("Jupiter", "Neptune"), ("Saturn", "Uranus"): ("Saturn", "Uranus"),
    ("Earth", "Mercury"),: ("Venus"),
    ("Mercury", "Uranus"): ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
}

for pair, res in test_bf.items():
    assert bf(*pair) == res
```