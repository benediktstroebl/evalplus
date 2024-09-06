Here's a Python script that solves the given problem with an efficient approach using dictionaries and an auxiliary helper function:
```python
def pluck(arr):
    even_nodes = {}
    for i, n in enumerate(arr):
        if n % 2 == 0:
            even_nodes.setdefault(n, []).append(i)
    
    if not even_nodes:
        return []

    min_index = None
    min_value = min(list(even_nodes.keys()))
    for idx in even_nodes[min_value]:
        if min_index is None or idx < min_index:
            min_index = idx
    
    return [min_value, min_index] if min_index is not None else []

# Test the solution
import unittest
class TestPluck(unittest.TestCase):
    
    def test_example1(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])
    
    def test_example2(self):
        self.assertEqual(pluck([1, 2, 3]), [2, 1])

    def test_example3(self):
        self.assertEqual(pluck([]), [])

    def test_example4(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

if __name__ == '__main__':
    unittest.main()
```

This code defines a `pluck` function that takes an array as input and returns the node with the smallest even value, along with its index in the array. The function first creates a dictionary, `even_nodes`, where the keys represent even values found in the array, and the values are lists of indices where those even values appear. If the array is empty or contains no even values, the function returns an empty list `[]`. Otherwise, it finds the minimum even value and its index using the `min` function and appropriate key selection from `even_nodes`. The function then returns a list containing the minimum even value and its index. 

The optional `TestPluck` class includes several test cases to verify the correctness of the `pluck` function against the problem statement's examples. It checks if the function returns the expected output for various test cases.  This allows you to run the tests and verify the function's behavior.  The `if __name__ == '__main__':` block at the end ensures that the test suite only runs when the script is executed directly and not when it's imported elsewhere, providing better test isolation.