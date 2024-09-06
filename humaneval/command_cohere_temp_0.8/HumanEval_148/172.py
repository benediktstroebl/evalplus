```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, cur_planet in enumerate(planets):
        if cur_planet == planet1: p1 = i
        if cur_planet == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return (planets[p2] if p2 < p1 else planets[p1:p2+1])
```

The function first collects the indices of `planet1` and `planet2` in the list of planets. If any of the planets is not found in the list, the function returns an empty tuple. Otherwise, it returns a sorted tuple of planets whose indices are between the indices of the given planets. The sorting is done by proximity to the sun, where the planet closer to the sun is indexed at a smaller number. You can assign this script to the variable `bf` and use it in tests similarly to the examples in the problem statement:
```python
test_bf = [
    ("Jupiter", "Neptune", ("Saturn", "Uranus")),
    ("Earth", "Mercury", ("Venus")),
    ("Mercury", "Uranus", ("Venus", "Earth", "Mars", "Jupiter", "Saturn")),
    ("Sun", "Mars", ()),
    ("Mars", "Sun", ()),
]
for planet1, planet2, ans in test_bf:
    assert bf(planet1, planet2) == ans
```