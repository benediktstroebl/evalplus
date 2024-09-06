```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -1, -10]
assert get_positive(input_list2) == [5, 3, 2, 3]

input_list3 = [5, 3, -5, 2, -3, 3, -10, -1, -100]
try:
    assert get_positive(input_list3) == [5, 3, 2, 3]
except Exception as e:
    print("Error:", e)
```