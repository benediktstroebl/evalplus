```python
def max_element(lst):
    if not_elements(lst):
        return None  # Empty list
    return max(lst, key=lambda x: x)

def not_elements(lst):
    return len(lst) > 0 and all(isinstance(x, int) for x in lst)

# Test the function
input = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(input))  # Output: 123
print(max_element([]) )  # Output: None
print(max_element([]))  # Output: None
print(max_element([1, 2, -5] ))  # Output: -5
```