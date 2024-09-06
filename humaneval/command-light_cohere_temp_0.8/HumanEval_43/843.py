```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum to zero, False otherwise.
    """
    first element in l is negative, return False
    """
    if first_num < 0:
        return False
    return all(num > 0 and sum(num) <= 0 for num in l)

#Test the function
test_passes = pairs_sum_to_zero([1, 3, 5, 0])
print("test_passes:",test_passes) # Output: False
test_passes = pairs_sum_to_zero([1, 3, -2, 1])
print("test_passes:",test_passes) # Output: False
test_passes = pairs_sum_to_zero([1, 2, 3, 7])
print("test_passes:",test_passes) # Output: True
test_passes = pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
print("test_passes:",test_passes) # Output: True
```
The function uses the condition to check if the first element is negative, if so, the function returns False, if not, it checks if all the numbers sum to zero, if so, the function returns True.