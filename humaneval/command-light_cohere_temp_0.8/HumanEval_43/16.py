```python
def pairs_sum_to_zero(lst):
    return any(x + y <= 0 for x, y in zip(lst, lst[1:])) and not any(x + y > 0 for x, y in zip(lst, lst[1:])))

# Example usage
my_list = [1, 3, 5, 0]
print(pairs_sum_to_zero(my_list))  # Output: False

my_list = [1, 3, -2, 1]
print(pairs_sum_to_zero(my_list))  # Output: False

my_list = [1, 2, 3, 7]
print(pairs_sum_to_zero(my_list))  # Output: False

my_list = [2, 4, -5, 3, 5, 7]
print(pairs_sum_to_zero(my_list))  # Output: True
```
This function determines whether the sum of any two elements in the list equals zero, and if so, it returns "True," otherwise, it returns "False."