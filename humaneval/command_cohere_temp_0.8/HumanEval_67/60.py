```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
```python
# TEST CASES
import unittest

class TestFruitDistribution(unittest.TestCase):
    def test_fruit_distribution_1(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
    def test_fruit_distribution_2(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
    def test_fruit_distribution_3(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
    def test_fruit_distribution_4(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
```
This code includes a test suite with multiple test cases to ensure the `fruits_distribution` function behaves as expected. In essence, the function extracts the number of apples and oranges from the input string, calculates the difference between the total number of fruits and the sum of apples and oranges, and returns this difference, which represents the number of mango fruits.