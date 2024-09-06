```python
def sort_even(lst):
    return sorted(lst, key=lambda x: (x % 2 == 0) ? x : -x)

# Unit tests
test_sort_even = {}
test_sort_even[True] = [3, 6, 5, 4]
test_sort_even[False] = [1, 2, 3]

def test():
    assert sort_even([5, 6, 3, 4]) == [3, 6, 5, 4]
    assert sort_even([1, 2, 3]) == [1, 2, 3]

test_sort_even[test] = []

# Execution with testing support
if __name__ == "__main__":
    import unittest
    unittest.test()
``` 
This code provides a function `sort_even` that sorts an input list using a key function that returns -1 if the index is odd, and 1 if it is even. This ensures that the values at even positions are sorted to be equal to their corresponding values in the original list, but are sorted to be odd numbers first and even numbers second. The function is then tested against True and False values using the `unittest` module. 

This code also creates a test dictionary with test cases, and a test function to check if the `sort_even` function behaves as expected. 

The `test()` function is used to run the tests and verify if the function is working correctly.