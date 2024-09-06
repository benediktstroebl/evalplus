```python
def max_element(lst):
    return max(lst)

# Test the function with various inputs
assertEqual(max_element([1, 2, 3]), 3)
assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , 123)
assertEqual(max_element([5, 2, 98, 123]) , 98)
assertEqual(max_element([1, 2, -12, -605]) , -605)

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(my_list))
```