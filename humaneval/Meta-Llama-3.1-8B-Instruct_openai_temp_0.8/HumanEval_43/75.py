```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    Parameters:
    l (list): A list of integers.
    
    Returns:
    bool: True if there are two distinct elements in the list that sum to zero, False otherwise.
    """
    return len(set([i for i in l if i!= 0 and -i in l])) > 0


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks if there are two distinct elements in the input list `l` that sum to zero. It uses a set comprehension to create a set of elements in `l` that have a corresponding negative element in `l`. It then checks if the length of this set is greater than 0, which means there are two distinct elements that sum to zero. If the length is 0 or 1, it returns False, indicating that there are no two distinct elements that sum to zero. 

The script also includes the test cases from the problem description to ensure that the function behaves as expected.