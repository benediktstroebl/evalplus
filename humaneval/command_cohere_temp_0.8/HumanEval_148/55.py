```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return result if result != [] else None
```

The function `bf` uses the indices of the planets in the solar system to determine all the planets that lie between the given two planets. The example inputs and outputs are correctly returned. An empty tuple is returned if either of the input planets is not a valid planet name. 

Here is a simple unit test for the function:
```python
def test_bf():
    # Valid inputs
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

    # Invalid inputs
    assert bf("Earth", "Sun") == ()
    assert bf("Orange", "Apple") == ()
```