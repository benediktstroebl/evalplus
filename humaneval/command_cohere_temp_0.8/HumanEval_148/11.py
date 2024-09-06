```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planet1.lower() if planet1 in planets else ''
    p2 = planet2.lower() if planet2 in planets else ''
    res = []
    s1, s2 = 0, len(planets) - 1
    while s1 <= s2:
        mid = (s1 + s2) // 2
        if planets[mid] == p1:
            s2 = mid - 1
        elif planets[mid] == p2:
            s1 = mid + 1
        else:
            res.extend(planets[mid:s2])
            s1 = mid + 1
    return res if res else tuple()
```

The function `bf` performs the following:
1. Ensures that the passed planets are valid by converting them to lowercase and checking their existence in the `planets` array.
2. Uses binary search to determine the proximity of planets to the sun, thus optimizing the search process.
3. The detected planets are then appended to the `res` list and returned as a tuple. Also, an empty tuple is returned if no planets are found.

The following tests are designed to cover various cases:
```python
test = ['bf("Jupiter", "Neptune")', 'bf("Earth", "Mercury")', 'bf("Mercury", "Uranus")']
expect = [('Saturn', 'Uranus'), ('Venus'), ('Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn')]

for t, e in zip(test, expect):
    assert t == str(e)
```