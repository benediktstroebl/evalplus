```python
def max_element(lst):
    return max(lst)

# Test the max_element function with various input lists
assertEqual(max_element([1, 2, 3]), 3)
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) ,123)
assertEqual(max_element([]) , 0)
assertEqual(max_element([1, 1, 1]) , 1)
```