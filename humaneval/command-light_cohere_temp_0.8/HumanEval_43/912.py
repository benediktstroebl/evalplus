```python
def pairs_sum_to_zero(l):
    return any(sum(a) == 0 for a in l)

# Example usage:
input_list = [1, 3, 5, 0]
result = pairs_sum_to_zero(input_list)
print(result)

input_list = [1, 3, -2, 1]
result = pairs_sum_to_zero(input_list)
print(result)

input_list = [1, 2, 3, 7]
result = pairs_sum_to_zero(input_list)
print(result)

input_list = [2, 4, -5, 3, 5, 7]
result = pairs_sum_to_zero(input_list)
print(result)
```

The script defines a function called `pairs_sum_to_zero` that takes a list of integers as input and checks if there exists any pair of integers in the list whose sum equals zero. The `any()` function is used to check this condition, and the result is returned.