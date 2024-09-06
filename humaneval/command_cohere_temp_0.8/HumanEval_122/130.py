Here's a Python script that contains a function to solve the given problem:
```python
def add_elements(arr, k):
    sum_two_digits = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum_two_digits += arr[i]
    return sum_two_digits

# Example usage
arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9]
k = 4
result = add_elements(arr, k)
print(f"Example output: {result}")

```

The function `add_elements` takes an array `arr` and an integer `k` as input, it iterates through the first `k` elements of the array and accumulates the sum of elements that have at most two digits. The result is then returned as the sum of these elements. 

The example usage demonstrates how to call the function with the provided input and prints the result. The output of the cell is:
```
Example output: 24
```

This result is achieved by the following line of code in the function:
```python
sum_two_digits += arr[i]
```

The unit test for this function would typically check various inputs to ensure that the function is calculating the sum correctly for a variety of cases.  This could be done using Python's `unittest` module, which is included in the Python standard library. 
For example, you might test with different lengths of the input array, different values of k, or different types of input elements, including integers of different sizes and other types of data that are unlikely to be relevant here. 
```python
import unittest

class TestAddElements(unittest.TestCase):
    def test_add_elements(self):
        # Test with some sample values
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), 21)
        self.assertEqual(add_elements([10, 11, 12, 13, 14, 15, 16, 17, 18], 5), 81)

        # Test with a different length of the array
        self.assertEqual(add_elements([10, 11, 12, 13, 14], 5), 61)

        # Test with a different value of k
        self.assertEqual(add_elements([10, 11, 12, 13, 14, 15, 16, 17, 18], 3), 51)

        # Test with some negative integers
        self.assertEqual(add_elements([10, -11, 12, -13, 14, -15, 16, -17, 18], 5), -59)

if __name__ == '__main__':
    unittest.main()
```
This code adds a test class TestAddElements, which defines a single test method called test_add_elements. This method calls the add_elements function with various inputs and verifies the results using self.assertEqual, this runs all the tests when the script is executed directly.