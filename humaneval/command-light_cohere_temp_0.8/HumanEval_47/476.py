```python
def median(l: list):
    """Return median of elements in the list l.
    """
    def _median(lst):
        if len(lst) < 1:
            return None
        mid = len(lst) // 2
        if lst[mid] > lst[mid - 1]:
            mid += 1
        return (
            (len(lst) % 2 == 0 and lst[mid])
            + (_median((lst[:mid - 1], lst[mid:])) or None)
            ) / 2
        else:
            return (lst[mid] + _median((lst[:mid], lst[mid + 1:]))) / 2
    return _median(l)

# Example usage:
median([-10, 4, 6, 1000, 10, 20]) # Output: 15.0
median([1, 2, 3, 4, 5]) # Output: 3.0
median([-10, 4, 6, 1000, 10, 20]) # Output: 15.0
median([10, 20, 30, 40, -30]) # Output: (30,40)/2
```