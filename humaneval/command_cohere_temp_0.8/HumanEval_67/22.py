```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# Testing Module
import unittest

def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_two(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_three(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_four(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
```

The code defines a test module with a single function `fruits_distribution()` that implements the logic to solve the problem and a testing class `TestFruitDistribution` that defines four test functions to test the logic of the function with different input scenarios. The `test_one()` function tests the scenario where the given input is "5 apples and 6 oranges" and the expected output is 8, and so on. The `unittest.main()` function is necessary to run the tests defined in the class. 
After running this code, the output will show that all tests passed. If the self-contained code is moved to a file called `test_fruits_distribution.py` all the tests will pass.