```python
def median(lst):
    # Sort the list in ascending order
    lst.sort()
    median = (len(lst) / 2)
    while len(lst) > median:
        lst.pop(lst.sort()
    copy = False
        # to handle empty list, median of an empty list is an undefined number.
    # return the time, lst is sorted, return the middle index of the sorted list
    return lst[median - 1]

# Test cases
test_median = [
    [
        [-10, 4, 6, 1000, 10, 20],
        [20, -10, 4, 6, 1000],
        [1000, 4, 6, -10, 10, 20],
        [1, 2, 3, 4, 5],
        ['abc', 'def', 'bcd']
    ]

for test in test_median:
    print(median(test))
```