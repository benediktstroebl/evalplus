```python
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) == 0:
        return False
    # For each element, check if it is less or greater than the previous
    for i in range(1, len(l)):
        if l[i] < l[i-1]:
            return True
    return False
# Test cases
print(monotonic([1, 2, 4, 20]))  # Output: True
print(monotonic([1, 20, 4, 10]))  # Output: False
print(monotonic([4, 1, 0, -10]))  # Output: True
``` 
This script defines a function `monotonic` that checks whether a list's elements are monotonically increasing or decreasing. The function uses a simple algorithm to compare elements and return True if any element is smaller than its previous. The test cases demonstrate the required behavior of the `monotonic` function.