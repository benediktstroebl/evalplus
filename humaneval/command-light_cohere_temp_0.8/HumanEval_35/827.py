```python
def max_element(lst):
    if not_num(lst):
        return 0
    return max(lst)

def not_num(lst):
    if not sorted(lst): return False
    return True

# Test cases
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
print(max_element([]))
print(max_element([1, 2, 3, -1000, 5, 6, 7])))
print(max_element([8, 9, -8]))
print(max_element([True, False, True]))
```
The function `max_element` in the above code snippet accepts a list `lst` as input. The function determines whether the particular number in the list using the `not sorted()` function. If the list is not sorted, the function returns `0`, which is regarded as an empty list. Otherwise, the function returns the maximum value from the list.

The following test cases are also passed to the `max_element` function to confirm its correctness.