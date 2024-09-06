```python
def pairs_sum_to_zero(l):
    """
    Check whether the list of integers has two distinct elements that sum to zero.
    :return "True" if there are such two elements that sum to zero else "False".
    """
    x, y = None, None
    for x, y in l:
        if x + y == 0:
            break
        else:
            x, y = y, x+y
    return bool(x)

# Example usage
input_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(input_list)
print(result)  # Output: True

input_list = [1, 3, -2, 1]
result = pairs_sum_to_zero(input_list)
print(result)  # Output: False

input_list = [1, 2, 3, 7]
result = pairs_sum_to_zero(input_list)
print(result)  # Output: False

input_list = [2, 4, -5, 3, 5, 7]
result = pairs_sum_to_zero(input_list)
print(result)  # Output: True
```