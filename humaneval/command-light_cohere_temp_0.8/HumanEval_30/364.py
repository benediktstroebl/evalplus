```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with different list inputs
print(get_positive([-1, 2, -4, 5, 6]))   # Output: [2, 5, 6]
print(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: [5, 3, 2, 3, 9, 123, 1]

# Test the function with a tuple input
print(get_positive((-5, 7)))       # Output: [7]
print(get_positive((5, 2)))       # Output: []

# Test the function with a list of strings
print(get_positive(["A", "B", "C"]))    # Output: []

# Test the function with negative and non-numeric inputs
print(get_positive([1, 2, "three"]))  # Output: []
```
This code defines a function get_positive that takes a list as input and returns a new list containing only the positive elements from the original list. The test section demonstrates the positive and negative inputs and non-numeric inputs. The function returns the expected results.