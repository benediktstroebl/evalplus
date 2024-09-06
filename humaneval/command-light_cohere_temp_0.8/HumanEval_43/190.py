```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    set of unique elements sum to zero and return True, otherwise False.
 # First test to ensure the list has two unique numbers that sum to zero. 
"""
nums = []
 for num in l:
    if len(set(nums)) != 2: 
       return False
    nums.append(num)
 return True 
```