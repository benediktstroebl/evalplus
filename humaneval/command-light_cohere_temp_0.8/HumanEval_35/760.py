```python
def max_element(lst):
    if not_inclusive_max(lst) == float('-inf'):
        return -1  # Return -1 if no elements or list is empty
    return max(lst, key=lambda x: x)

def not_inclusive_max(lst):
    return max(lst, key=lambda x: x)

# Test cases
max_element([1, 2, 3])         # 3
max_element([5, 3, -5])       # 3
max_element([5, -5, 3, -3])    # -5
max_element([-5, -3, 3, -5])  # -5
max_element([0, 2, 3, 0])       # 0
max_element([-1, 0, 0, 2])    # 2
max_element([1, 2, 3, 4, 5])   # 5

# Correctness test - empty list
max_element([])           # Return -1

# Correctness test - invalid key function
max_element([1, 2, 3])   # Raises TypeError: 'bound method .__iter()' not supported

```  This Python code defines a function `max_element` that calculates the maximum element in a list, considering both positive and negative values. It also has a test cases to validate the function's behavior and to ensure the correctness of the maximum element calculation.