```python
def max_element(lst):
    if not_element(lst) == -1:
        return -1
    return max(lst)

def not_element(lst):
    if isinstance(lst, list) and lst:
        return max(lst)
    return "not a list"

# Test the function
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])))
print(max_element([1, 2, 3, 'abc'])))
print(max_element([1, 2, 3, 'abc', 'def'])))
```
This Python code defines a function `max_element` that finds and returns the maximum element in a given list. It also includes a test cases to verify the function's behavior for different types of input lists.