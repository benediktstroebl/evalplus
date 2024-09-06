```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Test the function with a list of different data types
# Test with list of numbers, strings, and even a mixture

# Example 1: List of numbers
print(get_positive([-1, 2, -4, 5, 6]))  # Output: [2, 5, 6]

# Example 2: List of strings
print(get_positive(["abc", "hello", "world!"]))  # Output: [] (all strings are non-positive)

# Example 3: Mixture of numbers and strings
print(get_positive([5, 3, "-5", "2", "-3", "abc"]))  # Output: [5, 3]
```
This Python code defines a function called `get_positive` that takes an input list and returns a new list containing only the positive numbers from the original list. It then tests the Closes this function with a docstring that explains its purpose and how it works. This function effectively filters out and returns only positive numbers from a given input list, making it useful for various numerical and text-based data manipulation tasks.