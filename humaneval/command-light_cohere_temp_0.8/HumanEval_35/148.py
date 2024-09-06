```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test the function with a variety of data
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(my_list))  # Output: 123

my_list2 = [-5, 2, 4, -3, -10]
print(max_element(my_list2))  # Output: -10

my_list3 = [1, 2, 3]
print(max_element(my_list3))    # Output: 3
```