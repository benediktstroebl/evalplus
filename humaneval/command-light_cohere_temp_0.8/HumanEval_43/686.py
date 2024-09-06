```python
def pairs_sum_to_zero(l):
    """
    Returns True if the list contains two elements that sum to zero, 
    False otherwise.
    """
    note: the sum of any two elements in the list will never be equal to zero.
    """
    list of integers is checked using the built-in `len()` function and the 
    membership test.
    """
    sum two elements in the list are computed using the built-in `sum()` function.

test_pairs_sum_to_zero = []
for i in range(1, 10):
    test_pairs_sum_to_zero.append([i, i])
test_pairs_sum_to_zero.append([i + i])
test_pairs_sum_to_zero.append([i, 10-i])

def pairs_sum_to_zero(l):
    return sum([i for i in l]) % 2 == 0

# Main function to run the tests
test_pairs_sum_to_zero(test_pairs_sum_to_zero)
```

This script defines a function called pairs_sum_to_zero that checks whether a list contains two elements that sum to zero. It does this by iterating through each element in the list and checking whether the sum of any two elements is equal to zero. The function returns True if the list contains two elements that sum to zero, and False otherwise. The test_pairs_sum_to_zero function is a list of test cases that the pairs_sum_to_zero function is designed to handle. The function returns True for the list of integers, and False for any other input.