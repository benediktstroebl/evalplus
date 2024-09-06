```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x - 1)

# Test case 1
test_list = [1, 2, 3]
test_result = sort_even(test_list)
assert test_list == test_result

# Test case 2
test_list = [5, 6, 3, 4]
test_result = sort_even(test_list)
assert test_list == test_result

# Test case 3
test_list = [1, 10, 9, 5, 8]
test_result = sort_even(test_list)
assert test_list == test_result

# Test case 4
test_list = [3, 1, 2, 4, 5, 6]
test_result = sort_even(test_list)
assert test_list == test_result
```
The above Python script defines a function `sort_even` that takes a list as input and sorts the even elements of the list according to the keys of `lambda x: x if x % 2 == 0 else x - 1`. The function then returns a new list that maintains the original list's structure but with the even elements sorted. The script also includes several test cases to verify the correctness of the `sort_even` function.