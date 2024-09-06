```python
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
"""
    return sum(x) < 0 and set([x for x in l if x != l[-1]] + [l[-1]]) == set()
``` 
This solution checks for the condition that the sum of any two distinct elements in the list is less than zero, and returns True, indicating a solution. Otherwise, it returns False. 

Time complexity: O(n), where n is the number of elements in the list. 

Space complexity: O(1)