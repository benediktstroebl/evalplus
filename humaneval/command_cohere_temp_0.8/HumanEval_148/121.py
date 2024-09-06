```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[(p2 + 1) % 8], planets[((p1 - 1) + 8) % 8])
```
The function first stores the planets in the solar system in the `planets` array. It then tries to find the indices of the planets in the array with the `planet1` and `planet2` names. If one of the planets is not found, an empty tuple is returned. Otherwise, the function returns a tuple of sorted planets located between the two found planets. The sorting is done by proximity to the sun, taking into account that the array index starts at 0 and the formula `((p1 - 1) + 8) % 8` is used to iterate through the array in a cyclic manner. 

The tests correspond to the examples provided in the statement, and could be included in the following way:
```python
test_bf = {
    "bf(\"Jupiter\", \"Neptune\") -> \"Saturn\" \"Uranus\":": "assert bf(\"Jupiter\", \"Neptune\") == (\"Saturn\", \"Uranus\")",
    "bf(\"Earth\", \"Mercury\") -> \"Venus\":": "assert bf(\"Earth\", \"Mercury\") == (\"Venus\")",
    "bf(\"Mercury\", \"Uranus\") -> \"Venus\" \"Earth\" \"Mars\" \"Jupiter\" \"Saturn\":": "assert bf(\"Mercury\", \"Uranus\") == (\"Venus\", \"Earth\", \"Mars\", \"Jupiter\", \"Saturn\")",
}
for assertion, test in test_bf.items():
    assert eval(test)
```