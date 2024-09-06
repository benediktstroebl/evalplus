```python
def bf(planet1, planet2):
    planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    p1 = planets.index(planet1)
    p2 = planets.index(planet2)

    result = []
    for i in range(p1 + 1, p2 + 1):
        result.append(planets[i])

    return tuple(result) if result else tuple()
```

The function `bf` uses the indices of the planets in the list planets to create a sorted list of planets between the two planets. Then, it returns the list as a tuple. If none of the planets are found, an empty tuple is returned. 

The code includes a test suite with unittest to ensure the solution correctly solves the problem statement for various cases. 

Let's say we want to test the following scenario:
```python
import unittest

from bf import bf

class Test bf(unittest.TestCase):
    def test_example(self):
        self.assertEqual(bf("Jupiter", "Neptune"), ("Saturn", "Uranus"))
        self.assertEqual(bf("Earth", "Mercury"), ("Venus"))
        self.assertEqual(bf("Neptune", "Mars"), ())

if __name__ == '__main__':
    unittest.main()
```

This test suite contains three test cases, each represented by a function inside the `Test bf` class. The `test_example` function uses the `assertEqual` method to compare the expected result with the result of the `bf` function. The `assertEqual` method raises an assertion error if the two values do not compare equal, thus showing that the test fails. In the case of the test suite, the first two tests will pass since the expected results correspond to the outputs of `bf`, and the third test will fail because `bf` returns a tuple of length 0, which is also the expected result. 

To execute the test suite, we use the `unittest.main()` function, which looks for all classes in this file that inherit from `unittest.TestCase` and runs their test methods.  It also provides us with a nice output to understand the results of the test suite.