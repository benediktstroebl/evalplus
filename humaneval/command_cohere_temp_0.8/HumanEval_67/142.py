```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code uses the built-in Python `map` function to convert the apples and oranges strings into integer values, a `split` method is used to split the total count string into a list of strings, the `split` splits the string at the "and" symbol, the resulting list is converted back to a tuple using `tuple(..)` and is passed to the `map` function. The function then calculates the number of mangoes as the difference between the total number of fruits and the sum of apples and oranges and returns the result.

Here is the markdown code block with the corresponding tests:
```
```python
import unittest

def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
    def test_example2(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
    def test_example3(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
    def test_example4(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fruit_distribution("abc", 100)
    def test_negative_values(self):
        with self.assertRaises(ValueError):
            fruit_distribution("5 apples and 6 oranges", -10)
    def test_zero_total_fruits(self):
        with self.assertRaises(ValueError):
            fruit_distribution("5 apples and 6 oranges", 0)

if __name__ == '__main__':
    unittest.main()
```
```
The test class includes several test methods, each testing a specific scenario against the `fruits_distribution()` function. You can use the `unittest.main()` function to run all the test methods or select an individual method to focus on a specific test scenario.