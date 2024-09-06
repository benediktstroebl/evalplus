```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, the code then simply subtracts the sum of the apples and oranges from the total number of fruits to get the number of mangoes. The function is self-contained and can be executed independently.

Here is the code with corresponding tests:
```python
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