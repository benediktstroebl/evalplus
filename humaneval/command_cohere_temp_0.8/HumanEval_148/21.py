```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1, p2 = -1, -1
    for i, pole in enumerate(planets):
        if pole == planet1: p1 = i
        if pole == planet2: p2 = i
    if p1 == -1 or p2 == -1: return ()
    return tuple(planets[i] for i in range(p1, p2 + 1))
```

The function first collects the indices of `planet1` and `planet2` in the planets list, ignoring the inputs are not found in the list; otherwise, returns an empty tuple. You can test the code with the following snippet:
```python
import unittest
class TestBF(unittest.TestCase):
    def test_example(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
        self.assertEqual(bf("Mercury", "Uranus"), ("Venus", "Earth", "Mars", "Jupiter", "Saturn"))
if __name__ == '__main__':
    unittest.main()
``` 

The code can be explained as follows:
- The `planets` list contains the eight planets in our solar system, sorted by their proximity to the sun. 
- The function uses two for loops to find the indices of `planet1` and `planet2` in the `planets` list. The variables `p1` and `p2` are the indices of the planets sorted by the proximity to the sun.
- After finding the indices, the function returns a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun. If one or both inputs are not correct planet names, an empty tuple is returned. 
- The `bf` function can be used to solve the problem by passing two planet names as strings `planet1` and `planet2`. The function will return a tuple containing all planets whose orbits are located between the orbit of `planet1` and the orbit of `planet2`, sorted by the proximity to the sun. This approach doesn't require additional dependencies, quick and concise.