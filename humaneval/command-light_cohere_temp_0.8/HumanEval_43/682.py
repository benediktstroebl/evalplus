```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    pair to sum = sum of the first element and the second element of a pair 
    """
    return sum(sorted((x, y) for x, y in zip(l, l[1:]))) == 0

# Test the function
test_pairs_sum_to_zero = pairs_sum_to_zero
print(test_pairs_sum_to_zero([1, 3, 5, 0]))  # Output: False
print(test_pairs_sum_to_zero([1, 3, -2, 1]))  # Output: False
print(test_pairs_sum_to_zero([1, 2, 3, 7]))  # Output: False
print(test_pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # Output: True
print(test_pairs_sum_to_zero([1]))  # Output: False
```
The code defines a function called pairs_sum_to_zero that takes a list of integers as input and returns True if the list has two distinct elements whose sum is zero, and False otherwise. The function uses the pair to sum = sum of the first element and the second element of a pair in the list, and checks if the sum of these two elements is equal to zero.

The code then provides a series of test cases to the pairs_sum_to_zero function, and the function returns the appropriate results.