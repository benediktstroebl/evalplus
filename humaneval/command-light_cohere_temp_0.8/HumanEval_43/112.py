```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    lst = list(l)
    if len(set(lst)) == 2:
        return True
    else:
        return False
    """

# Test the function
test_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(test_list)
print(result)  # Output: True

test_list = [1, 3, -2, 1]
result = pairs_sum_to_zero(test_list)
print(result)  # Output: False

test_list = [1, 2, 3, 7]
result = pairs_sum_to_zero(test_list)
print(result)  # Output: False

test_list = [2, 4, -5, 3, 5, 7]
result = pairs_sum_to_zero(test_list)
print(result)  # Output: True
```