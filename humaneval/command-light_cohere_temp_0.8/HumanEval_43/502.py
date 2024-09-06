```python
def pairs_sum_to_zero(l):
    """
    checks if all pairs of elements in the list sum to zero, returns True if successful, False otherwise.
    """
   
    list comprehension, where elements[i] + elements[j] <= 0 for all i, j that are not i = j
    """
    return sum([x + y for x, y in zip(l, l)]) <= 0

#Example usage:
if pairs_sum_to_zero([1, 3, -2, 1]) == False:
    print("Solution does not exist!")

```
Do you have any other questions I can help you with?