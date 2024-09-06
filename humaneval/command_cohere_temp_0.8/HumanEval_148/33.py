```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    res = []
    for i in range(p1 + 1, p2 + 1):
        res.append(planets[i])

    return res if res != [] else None
```

The function first collects all planets in the solar system in the `planets` list, and then uses the `index` function to find the indices of `planet1` and `planet2`. It then completes the orbit between `planet1` and `planet2` and adds the planets to the `res` list, and returns the result. The special case is if `planet1` or `planet2` is incorrect, then `p1` and `p2` are out of range, and the result will be an empty list, which is handled by returning `None`. 

Here is a simple test suite for the function:
```python
def test_bf():
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    assert bf("Sun", "Pluto") == ()
    assert bf("Pluto", "Sun") == ()
```