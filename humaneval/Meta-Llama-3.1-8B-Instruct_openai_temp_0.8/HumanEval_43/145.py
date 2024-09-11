```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    
    :param nums: A list of integers.
    :return: A boolean indicating whether two distinct elements sum to zero.
    """
    num_set = set()
    for num in nums:
        if -num in num_set:
            return True
        num_set.add(num)
    return False


# Test cases
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This script defines a function `pairs_sum_to_zero` that checks for two distinct elements summing to zero in a list of integers. It does this by iterating over the list and checking if the negative of each number is in the set of numbers seen so far. If such a pair is found, the function immediately returns `True`. If it iterates over the entire list without finding such a pair, it returns `False`.

The script also includes the provided test cases to verify the function's correctness.