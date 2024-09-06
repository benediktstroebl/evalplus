```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```
This solution uses the split method to split the string into two strings ('apples' and 'oranges') and then calls the int() function to convert these into integers. It then returns the total number of fruits minus the number of apples and oranges. You can test this code by calling the function with various input values to ensure that it correctly calculates the number of mango fruits in the basket. 

Here is a test case example for the above code: 
```python
import unittest

def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_no_apples_oranges(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_negative_case(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_extra_test_case(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges",120), 19)
if __name__ == '__main__':
    unittest.main()
```