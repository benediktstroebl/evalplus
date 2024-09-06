```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code directly takes in the total number of fruits in the basket as a parameter and calculates the number of apples, oranges, and mango fruits by splitting the given string. It then returns the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.

Here is the accompanied test suite:
```python
import unittest

def fruit_distribution(s, n):
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