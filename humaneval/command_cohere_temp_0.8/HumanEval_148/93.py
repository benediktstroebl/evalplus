```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    if p1 == -1 or p2 == -1:
        return tuple()

    return tuple(planets[p] for p in range(max(p1, p2), min(p1, p2) + 1))
```

The function `bf` takes two planet names, `planet1` and `planet2`, as input and returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by their proximity to the sun. The function first creates a list of all planet names and uses `index` to find the positions of `planet1` and `planet2` in the list. The function then uses max and min together with range to iterate over all planets between the closerst and furthest planet to the sun of the two given planets. The function returns an empty tuple if either of the input planets is not a correct planet name. This is done by checking if the index of the planet name in the list is -1 which indicates that it is not found. 

Here is a simple test suite that can be used to verify the function:
```python
def test_bf():
    # test case 1
    planet1 = "Jupiter"
    planet2 = "Neptune"
    expected = ("Saturn", "Uranus")
    actual = bf(planet1, planet2)
    assert actual == expected

    # test case 2
    planet1 = "Earth"
    planet2 = "Mercury"
    expected = ("Venus")
    actual = bf(planet1, planet2)
    assert actual == expected

    # test case 3
    planet1 = "Mercury"
    planet2 = "Uranus"
    expected = ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    actual = bf(planet1, planet2)
    assert actual == expected

    # test case 4
    planet1 = "Sun"
    planet2 = "Moon"
    expected = tuple()
    actual = bf(planet1, planet2)
    assert actual == expected

test_bf()
```

The test suite includes four tests, testing the cases where the input planets are correct, one of the input planets is incorrect, the planets are furthest from each other in the solar system, and when they are closest to each other.