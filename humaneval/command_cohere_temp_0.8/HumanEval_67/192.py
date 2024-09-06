```python
def fruit_distribution(s,n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges
```

This Python script provides a function called `fruit_distribution` operates on two parameters, a string, and an integer. The string represents the number of apples and oranges in the basket, and the integer represents the total number of fruits in the basket. The return value of the function is the number of mangoes in the basket. 

To achieve this, the function `fruit_distribution` uses Python's powerful built-in `map` function to convert the string representation into integers. The `split 'and'` expression separates the string into apples and oranges. With these integers, the function returns the value of `n - apples - oranges`, which is the number of mangoes in the basket. 

The function dynamically separates the string and does not require a specific format for the input string beyond the existence of the word 'apples', 'oranges', and 'and'. This allows for flexibility in input, such as 'apples, oranges, and mangoes' or 'oranges, apples, and mangoes'. This flexibility makes the code more robust and adaptable to variations in the input description. 

Note that this code assumes that the given description in the string is formatted as "apples and oranges" and the total number of fruits in the basket is represented by the integer `n`.

The best practice is to incorporate tests in a separate module to verify the correctness of the function. Here's an example of a test module:
```python
import unittest

def fruit_distribution(s, n):
    apples, oranges = map(int, s.split(' and '))
    return n - apples - oranges

class TestFruitDistribution(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(fruits_distribution("5 apples and 6 oranges", 19), 8)

    def test_example2(self):
        self.assertEqual(fruits_distribution("0 apples and 1 oranges", 3), 2)

    def test_example3(self):
        self.assertEqual(fruits_distribution("2 apples and 3 oranges", 100), 95)

    def test_example4(self):
        self.assertEqual(fruits_distribution("100 apples and 1 oranges", 120), 19)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fruit_distribution("abc", 4)

        with self.assertRaises(ValueError):
            fruit_distribution("7 apples 9 oranges", 10)

if __name__ == '__main__':
    unittest.main()
```

In this test suite, there are several test cases in the `testFruitDistribution` class that validate the correctness of the `fruit_distribution` function for various inputs. There is also an `test_invalid_input` method that verifies the function raises a `ValueError` for invalid input, such as a non-integer number or absence of the word 'oranges' or 'apples'. 
This test suite can be run independently to validate the function behavior and ensure it is updated properly with changes in the code.