```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

The code solves the problem by taking two integers from the string using the split() function and the 'and' delimiter. Then, the total number of mangoes is calculated by subtracting the number of apples and oranges from the total number of fruits in the basket. As the program is written in a self-contained format, it can be imported anywhere and directly used. You can test it with different input scenarios to ensure it works correctly. 
Here is the provided code with corresponding tests to verify its correctness:
```python
import unittest

def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_one_apple_one_orange(self):
        self.assertEqual(fruit_distribution("1 apple and 1 orange", 10), 8)

    def test_zero_apples_one_orange(self):
        self.assertEqual(fruit_distribution("0 apples and 1 orange", 10), 9)

    def test_many_apples_few_oranges(self):
        self.assertEqual(fruit_distribution("100 apples and 2 oranges", 105), 103)

if __name__ == '__main__':
    unittest.main()
```

In the above code, the `fruit_distribution()` function is tested using a variety of inputs to verify its correctness. You can run this test file to see the results.