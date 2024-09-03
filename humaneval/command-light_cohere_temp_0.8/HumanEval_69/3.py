```python
def search(lst):
    """Return the greatest integer that occurs more than zero times in the list, or -1 if no such integer exists."""
    freq = 1 # Initialize frequency counter.
    for num in lst:
        freq += 1
    return max([num for num in lst if num > 0 and freq == num]) or -1
```
This solution defines a function called `search` which returns the greatest integer that appears more than zero times in the list, or -1 if no such integer exists. The function uses a frequency counter to count the number of times each integer appears in the list.