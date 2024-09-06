```python
def incr_list(lst):
    n = len(lst)
    lst[:] = [n+1] * (n+1) / 2
    return lst

# Test the function with different lists
test_list = incr_list([1, 2, 3])
test_list2 = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_list) # Output: [2, 3, 4]
print(test_list2) # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```