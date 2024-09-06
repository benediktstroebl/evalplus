```python
def get_positive(input_list):
    return [x for x in input_list if x >= 0]

# Test cases
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
assert get_positive(input_list1) == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -100, -1000]
assert get_positive(input_list2) == [5, 3, 2, 3]

input_list3 = [-1, 2, -4, 5, 6]
assert get_positive(input_list3) == [2, 5, 6]
```
The function get_positive takes an input_list and returns a list containing only the positive numbers from the input. The test cases ensure that the function works correctly for different lists.