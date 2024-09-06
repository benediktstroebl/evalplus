```python
def max_element(lst):
    return max(lst)

# Test case 1: Basic list
print(max_element([1, 2, 3]))  # Output: 3

# Test case 2: List of negative numbers
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, -10]))  # Output: 123

# Test case 3: List with duplicate elements
print(max_element([5, 3, 3, 2, 3, 9, 0, 123]))  # Output: 3

# Test case 4: Empty list
print(max_element([]))

# Test case 5: List with one element
print(max_element([5]))  # Output: 5
```
This script defines a function `max_element` that takes a list as input and returns the maximum element from that list using the `max()` function from the built-in `math` module. The script then passes various test cases and prints the result of the function for each case.