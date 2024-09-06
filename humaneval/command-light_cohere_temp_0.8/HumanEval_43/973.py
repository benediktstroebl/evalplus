```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    False otherwise.
    """
    def check_sum(num1, num2):
        return num1 + num2 == 0
    return any(check_sum(num1, num2) for num1, num2 in zip(l, l[1:] + [0]))
```
The function checks whether any two distinct elements in the list sum to zero, and returns True or False accordingly.