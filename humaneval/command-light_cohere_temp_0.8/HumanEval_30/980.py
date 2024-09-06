```python
def get_positive(input_list):
    return [num for num in input_list if num >= 0]

# Test the function with different input lists
input_list1 = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result1 = get_positive(input_list1)
assert result1 == [5, 3, 2, 3, 9, 123, 1]

input_list2 = [5, 3, -5, 2, -3, 3, -1, 1, -10]
result2 = get_positive(input_list2)
assert result2 == [5, 3, 2, 3, -1]

input_list3 = [-1, 2, -4, 5, 6]
result3 = get_positive(input_list3)
assert result3 == [2, 5, 6]
```
The Python script defines a function `get_positive` that takes an input list and returns a new list containing only the positive numbers from the input. It then tests the regular expression `[] >= 0` is used to filter out negative numbers from the input list, which are then returned.