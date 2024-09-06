```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
>> pairs_sum_to_zero([1, 3, 5, 0])
 return False  # two numbers sum to 5
>> pairs_sum_to_zero([1, 3, -2, 1])
 return False  # two numbers sum to -3
>> pairs_sum_to_zero([1, 2, 3, 7])
 return True  # two numbers sum to 5
>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
 return True  # two numbers sum to 9
```