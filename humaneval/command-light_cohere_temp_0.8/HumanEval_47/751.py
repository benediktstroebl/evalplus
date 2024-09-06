```python
def median(lst):
    """Return median of elements in the list lst."""
    # Sort the list in ascending order
    lst.sort()
    number of elements = len(lst)
    m = int((len(lst) + 1) / 2)
    for i in range(m):
        if lst[i] > lst[i + m]:
            lst[i], lst[i + m] = lst[i + m], lst[i]
    if lst[0] <= lst[m - 1]:
        return lst[m]
    return lst[m - 1]

# Test cases
test_median = [
    [[-10, 4, 6, 1000, 10, 20],
    [1, 2, 3, 4, 5],
    [0, 2, 4, 6, 8, 10, 20],
    [1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10],
]

for test_case in test_median:
    print(f"Test case {test_case} median: {median(test_case)}")
``` 
This script defines a function median that computes the median of a given list of numbers, and passes various test cases with different numbers. The output will display the