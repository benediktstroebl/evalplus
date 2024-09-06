Here's a Python script with a self-contained function that solves the problem:
```python
def monotonic(lst):
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, len(lst) - 1, (lo + hi) // 2
    if lst[mid] > lst[mid + 1]:
        return monotonic(lst[mid + 1:]) and monotonic(lst[:mid])
    if lst[mid] < lst[mid + 1]:
        return monotonic(lst[:mid]) and monotonic(lst[mid + 1:])
    return monotonic(lst[mid + 1:]) or monotonic(lst[:mid])
```
This code defines a Python function named 'monotonic' that checks whether a list contains monotonically increasing or decreasing elements. It handles the base cases of an empty list or a list with one element correctly. Then, it uses a binary search algorithm to efficiently determine the midpoint of the list. After that, it compares the element at the midpoint with the element immediately after it to determine the list's monotonic behavior. Finally, it recursively checks the monotonic properties of the list's left and right halves. The function returns 'True' if the list is monotonic and 'False' otherwise. Overall, this code efficiently solves the monotonicity checking problem for lists.