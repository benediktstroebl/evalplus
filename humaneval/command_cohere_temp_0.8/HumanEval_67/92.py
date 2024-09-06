```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This problem can be solved by parsing the string input with the split() method to convert the string representation of apples and oranges into integers. After obtaining the number of apples and oranges, these quantities are subtracted from the total number of fruits in the basket (represented by the integer n) to find the number of mango fruits in the basket. An example test case for this script could be:
```python
test_case = [
    ("5 apples and 6 oranges", 19),
    ({"Input": "5 apples and 6 oranges", "Target": 8}),
]
```

```python
import unittest

def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_one_example(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_second_example(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_third_example(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_fourth_example(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
```

This would test four different examples of input to ensure the function fruit_distribution() correctly solves the problem.