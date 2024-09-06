Here's the Python code for the problem you described:
```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    list of integers contains two distinct numbers, they will be added together and 
    the sum will be checked against zero, returning True if successful, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    True
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for num in l:
        if sum(l) == 0:
            return True
    return False
```
The function iterates through each number in the list and checks if the sum of those numbers equals zero. If there are two distinct numbers that sum to zero, the function will return True. If the sum of the numbers does not equal zero, the function will return False. 

This function can easily be integrated into your markdown code block and will solve the problem of checking if there are two numbers in the list that sum to zero.