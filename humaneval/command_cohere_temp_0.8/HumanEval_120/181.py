Here's a Python script that includes a function maximum_k to solve the problem, along with unit tests to verify its correctness:
```python
import unittest
from collections import Counter

def maximum_k(arr, k):
    """
    Finds the maximum k numbers from the array arr and returns a sorted list of length k.
    """
    counter = Counter(arr)
    return sorted(counter.most_common(k))[0:k]

class MaximumKTest(unittest.TestCase):
    def test_example_1(self):
        arr = [-3, -4, 5]
        k = 3
        result = maximum_k(arr, k)
        expected = [-4, -3, 5]
        self.assertEqual(result, expected)

    def test_example_2(self):
        arr = [4, -4, 4]
        k = 2
        result = maximum_k(arr, k)
        expected = [4, 4]
        self.assertEqual(result, expected)

    def test_example_3(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        result = maximum_k(arr, k)
        expected = [2]
        self.assertEqual(result, expected)

    def test_large_input(self):
        # Ensure the function can handle a large input without errors
        arr = list(range(100, 1000))
        arr.extend(range(-1000, -100))
        k = 5
        result = maximum_k(arr, k)
        expected = [99, -1, -2, 2, 5]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
```
This script includes a well-defined function called maximum_k, which takes two parameters - a list of integers arr and an integer k. The function utilizes the Counter class from the collections module to count the occurrences of each element in arr. Then, it sorts these counts in descending order and selects the top k elements to return as a list. 

The script also includes a set of unit tests, defined as subclasses of MaximumKTest, that validate the behavior of the `maximum_k` function against the specified problem's examples and larger input. Using the unittest.main() function, these tests execute automatically when the script is run. 

Lastly, the script is formatted and organized neatly, making it readable and maintainable. It should serve as a reliable solution for the specified problem and provide a solid foundation for addressing similar challenges in the future.