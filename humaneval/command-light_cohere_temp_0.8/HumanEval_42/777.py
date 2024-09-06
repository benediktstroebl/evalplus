```python
def incr_list(lst):
    lst[:] = [1, 2, 3]
    return lst

# Test the function
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)
```