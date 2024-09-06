Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi = l[0], l[-1]
    for i in range(1, len(l)-1):
        if (hi < l[i] < lo) or (lo < l[i] < hi):
            return False
        if l[i] == lo and l[i] == hi:
            return False
        lo, hi = hi, l[i]
    return True
```

The function `monotonic()` checks if the list of elements is monotonically increasing or decreasing. The function first handles the edge case of an empty or single-element list, returning True in both cases. For longer lists, the code employs two pointers, `lo` and `hi`, initialized to the first and last list elements, respectively. It then iterates through the list, checking if each element is strictly between `lo` and `hi`. If so, the function reiterates with updated pointers `hi` and `lo`. If the current element is equal to `lo` or `hi`, the list is not monotonically changing and the function returns False. Otherwise, the pointers are updated and the function continues checking through the list. Ultimately, if the function reaches the end of the list without encountering any inconsistencies, it returns True, indicating a monotonically changing list.  The total time complexity of the provided solution is O(n), where n is the length of the input list.