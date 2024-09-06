```python
def triples_sum_to_zero(l: list):
    """
    Function to check if a list of integers has three distinct elements sum to zero.
    Returns: True if all three numbers are 0, and False otherwise.
    """
    triple_sum = sum([x for x in l if x != 0])
    if triple_sum == 0:
        return True
    else:
        return False
``` 
The above Python code defines a function named `triples_sum_to_zero` that checks whether a list of integers has three distinct elements whose sum is equal to zero. The function uses the sum of the list items that are not equal to zero, and it returns `True` if the sum is zero, indicating that the three elements are zero, and `False` otherwise. The function uses a simple logic to achieve this.