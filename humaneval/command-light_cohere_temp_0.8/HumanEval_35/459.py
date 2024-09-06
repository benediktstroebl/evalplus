```python
def max_element(lst):
    if not_elements(lst):  # Check for empty list
        return None
    return max(lst, default=float('-inf'))

def not_elements(lst):
    return not len(lst) == 0

# Tests
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)
assertEqual(max_element([]) , None)
assertEqual(max_element([::y]) , None)
# Benchmarks
print("Success!")
```