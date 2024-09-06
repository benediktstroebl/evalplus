```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Unit tests
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, -6, -7, -50, 0, int('Hello')]
try:
    assert get_positive(input_list2) == []
    raise AssertionError
except AssertionError as e:
    print(e)
```