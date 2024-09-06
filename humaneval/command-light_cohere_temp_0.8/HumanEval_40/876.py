```python
def triples_sum_to_zero(lst):
    """
    Returns True if there are three distinct elements in lst that sum to zero, 
    otherwise, False. specific list of integers as input.
    """
 triple_sum = sum([x for x in lst if lst.count(x) < 3])
    return sum(x == triple_sum) <= 0
``` 
The function checks if there are three distinct elements that sum to zero in the list, if the condition is met, then it returns True; otherwise, it returns False.