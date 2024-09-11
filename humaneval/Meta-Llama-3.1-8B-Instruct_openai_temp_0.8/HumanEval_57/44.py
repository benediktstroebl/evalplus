```python
def monotonic(l: list):
    """
    Return True if list elements are monotonically increasing or decreasing.
    
    A list is monotonically increasing if every pair of consecutive elements
    satisfies the condition that the first element is less than or equal to the second.
    
    A list is monotonically decreasing if every pair of consecutive elements
    satisfies the condition that the first element is greater than or equal to the second.
    
    Args:
    l (list): A list of numbers.
    
    Returns:
    bool: True if the list is monotonically increasing or decreasing, False otherwise.
    """
    return all(x <= y for x, y in zip(l, l[1:])) or all(x >= y for x, y in zip(l, l[1:]))

# Test cases
print(monotonic([1, 2, 4, 20]))  # True
print(monotonic([1, 20, 4, 10]))  # False
print(monotonic([4, 1, 0, -10]))  # True
print(monotonic([1, 3, 2, 4]))    # False
print(monotonic([1, 1, 1, 1]))    # True
print(monotonic([5, 3, 2, 1]))    # False
print(monotonic([10, 5, 5, 1]))   # False
print(monotonic([1, 5, 2, 3]))    # False
print(monotonic([1, 2, 3, 4, 5])) # True
```
This script uses the `all()` function along with generator expressions to check for both increasing and decreasing sequences. The `zip(l, l[1:])` expression pairs each element with the next one in the list, and the generator expressions check if the pairs are in ascending or descending order. If either of these is true for the entire list, the function returns `True`. Otherwise, it returns `False`.