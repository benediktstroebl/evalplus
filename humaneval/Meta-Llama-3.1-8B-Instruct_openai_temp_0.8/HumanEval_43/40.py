### pairs_sum_to_zero function in Python

Here is a Python function that solves the problem using a set to store the numbers we have seen so far. This allows us to check in constant time if a number's negation is in the set.

```python
def pairs_sum_to_zero(nums):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()  # a set to store the numbers we have seen so far
    for num in nums:
        if -num in seen:  # if the negation of the current number is in the set
            return True  # return True because we found two numbers that sum to zero
        seen.add(num)  # add the current number to the set
    return False  # if we finished iterating over the list and didn't find two numbers that sum to zero, return False

# Example usage:
print(pairs_sum_to_zero([1, 3, 5, 0]))  # False
print(pairs_sum_to_zero([1, 3, -2, 1]))  # False
print(pairs_sum_to_zero([1, 2, 3, 7]))  # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))  # True
print(pairs_sum_to_zero([1]))  # False
```

This function works by iterating over the input list and checking if the negation of each number is in the set. If it is, we return True because we have found two numbers that sum to zero. If we finish iterating over the list and haven't found any such pair, we return False. This function has a time complexity of O(n) because it makes one pass over the input list and uses a set to store the numbers we have seen so far.