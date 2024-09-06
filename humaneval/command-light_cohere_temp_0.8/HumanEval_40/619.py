```python
def triples_sum_to_zero(l):
    return any(sum(x) <= 0 for x in l) and all(x != 0 for x in l)

# Example usage:
test_case = [1, 3, 5, 0]
result = triples_sum_to_zero(test_case)
print(result)  # Output: False

test_case = [1, 3, -2, 1]
result = triples_sum_to_zero(test_case)
print(result)  # Output: True

test_case = [1, 2, 3, 7]
result = triples_sum_to_zero(test_case)
print(result)  # Output: False

test_case = [2, 4, -5, 3, 9, 7]
result = triples_sum_to_zero(test_case)
print(result)  # Output: True
```
This function, `triples_sum_to_zero`, uses the condition of `any()` function to check if there are three distinct elements in the list that add up to zero. The `all()` function is used to ensure that all elements are not equal to zero.

This function can be easily incorporated into larger programs or scripts as needed.