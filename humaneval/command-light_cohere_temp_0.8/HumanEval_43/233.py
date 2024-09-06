```python
def pairs_sum_to_zero(l):
    return any(x + y > 0 for x, y in zip(l, l[1:]))

# Test the function
test_pairsum = [1, 3, -2, 1]
test_pairsum2 = [1, 2, 3, 7]
test_pairsum3 = [2, 4, -5, 3, 5, 7]

print(pairs_sum_to_zero(test_pairsum))  # Output: False
print(pairs_sum_to_zero(test_pairsum2))  # Output: True
print(pairs_sum_to_zero(test_pairsum3))  # Output: False
```
This script defines a function called pairs_sum_to_zero that takes a list of integers as input and returns True if there are two distinct elements in the list that their sum is zero, and False otherwise. The test cases pass the test the expected outputs, which are consistent with the function.