```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    sum of two integers a and b from the list is: a + b = sum_list
    """
    return sum_list(l) == 0

# Test cases
test_pairs_sum_to_zero = []
test_pairs_sum_to_zero.append([1,3, -2,1])
test_pairs_sum_to_zero.append([2,4,1,3,7])
test_pairs_sum_to_zero.append([2,5,3,7,8])
test_pairs_sum_to_zero.append([6,5,6,7])

# Function call and test result printing
print(pairs_sum_to_zero(test_pairs_sum_to_zero))
```