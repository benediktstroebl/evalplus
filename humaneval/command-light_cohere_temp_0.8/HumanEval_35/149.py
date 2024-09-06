```python
def max_element(lst):
    if not_numbers(lst):
        return float('-inf')  # No positive or negative numbers
    elif len(lst) == 0:
        return float('-inf')  # Base case: empty list
    max_element = lst[0]
    for num in lst[1:]:
        if num > max_element:
            max_element = num
    return max_element

def test_max_element(test_list):
    expected = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    actual = max_element(test_list)
    assert actual == expected, "max_element did not return the correct value"

# Example usage
my_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = max_element(my_list)
print(result)  # Output: 123
```
The function `max_element` calculates the maximum element in a list. The function `test_max_element` provides tests to check the correctness of the `max_element` function. The `max_element` function uses the base case of an empty list and then uses an iterative approach to compare and update the maximum element in the list.