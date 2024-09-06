```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```

This Python script defines a function `unique` that takes a list `l` as an argument and returns a sorted list of unique elements present in `l`. The algorithm to solve this problem uses the following steps:
1. Convert the list to a set to remove duplicate elements.
2. Convert the set back to a list.
3. Sort the list.
4. Return the sorted list.

This approach efficiently solves the problem using built-in Python data structures and operations, ensuring uniqueness and preserving the order of elements.

The unit tests for this function can be defined using the `unittest` module, and the function can be validated using the example test case provided in the problem statement. 

For example, you can use the following code to test the `unique` function:
```python
import unittest

def test_unique():
    # Test case from the problem statement
    input_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected_result = [0, 2, 3, 5, 9, 123]
    result = unique(input_list)
    assert result == expected_result
    assert len(result) == len(set(input_list))  # Additional assertion for uniqueness

if __name__ == '__main__':
    unittest.main()
```

In this example, `unittest` is imported, and a test function named `test_unique` is defined. This function calls the `unique` function with the input list from the problem statement and compares the result with the expected result using the `assert` statement. 

Additionally, an assertion is made to verify that the resulting list has the same number of elements as the input list's unique elements. 

When you run this test script, the `unittest` module executes the `test_unique` function, ensuring that the `unique` function returns the expected result and operates correctly.  Any assertion failure triggers an error, highlighting the issues in the function's implementation.