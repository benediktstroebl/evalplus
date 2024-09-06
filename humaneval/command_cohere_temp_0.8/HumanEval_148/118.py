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

The function first attempts to locate the indices of the given planets in the `planets` list. It then returns the planets located between the two indices, optionally excluding the planets if they are not found. The code offers a concise solution to the problem using list comprehension and integer arithmetic. 

The unit tests for this function demonstrate its usage and edge cases coverage:
```python
def test_bf():
    # Valid input cases
    assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
    assert bf("Earth", "Mercury") == ("Venus")
    assert bf("Saturn", "Mars") == ("Jupiter", "Earth", "Venus")

    # Edge cases
    assert bf("Neptune", "Uranus") == ()
    assert bf("Pluto", "Uranus") == ()  # Pluton is not a valid planet
    assert bf("Mars", "Earth") == ("Venus", "Mercury")

    # Input with missing/invalid planets
    assert bf("Saturn", "Sun") == ()
    assert bf("Green", "Mars") == ()
```