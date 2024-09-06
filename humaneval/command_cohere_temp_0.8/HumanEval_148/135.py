```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return result if result else None
```

The function first collects all planets in the solar system in the `planets` list, and then uses Python's `index` function to determine the relative positions of `planet1` and `planet2`. It then iterates through the positions in between and adds the planets to the `result` list. The resulting list is returned, but checked for emptiness and replaced with `None` to accommodate the final specification. 

The test cases are written as follows:
```python
test_cases = [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
]

for planet1, planet2, test_result in test_cases:
    assert bf(planet1, planet2) == test_result
```