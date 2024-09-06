```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x+1)

# Test cases
test_list = [1, 2, 3, 5, 6, 4]
test_result = sort_even(test_list)
assert test_result == [3, 5, 4, 6, 1, 2]

test_list = [5, 6, 3, 4, 7]
test_result = sort_even(test_list)
assert test_result == [3, 6, 5, 4, 7]

test_list = [5, 6, 3, 'four', 4, 'three']
test_result = sort_even(test_list)
assert test_result == [3, 6, 'four', 5, 7]
```
The function `sort_even` sorts the list based on whether each element is even or odd. It uses the value of the elements to determine if they are even or odd, and then sorts the list accordingly.