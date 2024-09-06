```python
def sort_even(l: list):
    return sorted(l, key=lambda x: x if x % 2 == 0 else x + 1)

# Test the function
test_list = [5, 6, 3, 4]
result = sort_even(test_list)
assert result == [3, 6, 5, 4]
test_list2 = [1, 2, 3]
result2 = sort_even(test_list2)
assert result2 == [1, 2, 3]
```
The function `sort_even` sorts the list `l` such that the odd index is the same in the original list and the new list, while the even index is one more than the original. It uses the `key=lambda x: x if x % 2 == 0 else x + 1` to achieve this.