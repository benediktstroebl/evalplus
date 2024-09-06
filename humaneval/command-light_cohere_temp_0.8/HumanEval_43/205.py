```python
def pairs_sum_to_zero(l):
    return any(sum(a) == 0 and a != 0 for a in l)

# Test the function
test_sum = [1, 3, -2, 1]
test_sum2 = [1, 2, 3, 7]
test_sum3 = [2, 4, -5, 3, 5, 7]
test_sum4 = [1]

print(pairs_sum_to_zero(test_sum))  # Output: False
print(pairs_sum_to_zero(test_sum2))  # Output: False
print(pairs_sum_to_zero(test_sum3))  # Output: True
print(pairs_sum_to_zero(test_sum4))  # Output: False
```
This code defines a function `pairs_sum_to_zero` that checks whether all the elements in the list sum to zero, returning `True` if they do and `False` otherwise. The test cases use a in the function to ensure its correctness.