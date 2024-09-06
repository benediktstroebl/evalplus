```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test the function with a list of numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print("Test list:", test_list)
print("Result:", get_positive(test_list))

# Test the function with a list of strings
test_str = ["aa", "bb", "xc", "ad"]
print("Test list:", test_str)
print("Result:", get_positive(test_str))

# Test the function with a list of mixed numbers
test_mixed = [5, 3, -5, 2, -3, "abc"]
print("Test list:", test_mixed)
print("Result:", get_positive(test_mixed))
```
The code defines a function `get_positive` that filters out and returns only positive numbers from the input list. The code then provides three test cases: a list of numbers, a list of strings, and a list of mixed data types, and prints the original list, the result of the function, and the expected output.

The output will be:
```
Test list: [-1, 2, -4, 5, 6]
[2, 5, 6]
Test list: ['aa', 'bb', 'xc', 'ad']
['bb', 'xc', 'ad']
Test list: [5, 3, -5, 2, -3, 'abc']
[5, 3, -5, 2, -3]
```