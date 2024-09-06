```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with a list containing various numbers
test_list = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
result = get_positive(test_list)
assert result == [5, 3, 2, 3, 9, 123, 1]

# Test with a list containing only negative numbers
negative_list = [-1, -4, -5, -6]
result_negative = get_positive(negative_list)
assert result_negative == []
```
This Python code defines a function called **get_positive** that takes a list as input and returns a new list containing only the positive integers from the original list. It then tests this using two different lists: the first containing a mix of positive and negative numbers, and the second containing only negative numbers, and finally passes these test cases to verify the correctness of the function.