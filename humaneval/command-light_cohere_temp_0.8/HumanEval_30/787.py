```python
def get_positive(input_list):
    positive = [num for num in input_list if num > 0]
    return positive

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123]

input_list2 = [5, 3, -5, 2, -3, 3, -10]
assert get_positive(input_list2) == [5, 3, 2]

input_list3 = [5, 3, -5, 2, -3, 3, -5, -1]
assert get_positive(input_list3) == [-5, 2, -3]
```