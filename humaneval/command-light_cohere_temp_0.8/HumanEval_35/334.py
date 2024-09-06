```python
def max_element(lst):
    if not_positive(lst) and not_empty(lst):
        return max(lst)
    else:
        raise ValueError("Input list must contain positive numbers")

def not_positive(lst):
    return all(x > 0 for x in lst)

def not_empty(lst):
    return len(lst) == 0

# Test the function with a variety of inputs
try:
    max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
except ValueError as e:
    print("Error:", str(e))

# Test input validity
try:
    max_element([1, 2, 3])
except ValueError as e:
    print("Error:", str(e))

try:
    max_element([0])
except ValueError as e:
    print("Error:", str(e))

try:
    max_element([-5, -10, 0, -20])
except ValueError as e:
    print("Error:", str(e))
```
The code defines a function `max_element` that takes a list as input and returns the maximum element in the list. The `not_positive` function checks whether the input list contains only positive numbers, and the `not_empty` function checks if the list is empty. The code also includes test cases to verify the correctness of the `max_element` function and validate the input.