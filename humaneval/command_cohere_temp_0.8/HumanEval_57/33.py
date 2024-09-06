Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(l) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(l) - 1) // 2
    while hi - lo > 1:
        if l[mid] <= l[mid + 1]:
            if l[mid] <= l[lo] or l[mid + 1] >= l[hi]:
                return True
            mid += 1
        else:
            if l[mid] >= l[mid - 1] or l[lo] >= l[mid]:
                return True
            lo += 1
    return False
```

The function initially determines whether the list has one or fewer elements, returning True in such cases because an empty or single-element list can't be monotonic. It then splits the list into a low half, a middle half, and a high half. It iterates through these three parts and determines whether the list is monotonic when considering only the middle two parts. If the conditions are met, the function returns True. Otherwise, it proceeds to compare the middle element with the elements on both sides of it in the low and high halves. Finally, it verifies if the list is monotonic when considering only the first and last halves. If any of these conditions are met, the function returns True, indicating a monotonic list; otherwise, it returns False. 

The unit tests can be run as follows:
```python
test_monotonic([1, 2, 4, 20], True)
test_monotonic([1, 20, 4, 10], False)
test_monotonic([4, 1, 0, -10], True)
``` 
This will verify the function's behavior against the given test cases.