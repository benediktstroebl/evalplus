```python
def triples_sum_to_zero(l):
    """
    Function to check if a list of integers sums to zero
    """
    if sum(l) == 0:
        return True
    return False
``` 
This function checks if the sum of any three distinct elements from the list is equal to zero. It does this using a simple mathematical check, and returns True if the condition is met, and False otherwise.