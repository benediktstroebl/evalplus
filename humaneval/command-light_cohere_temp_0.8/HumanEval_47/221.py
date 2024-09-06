```python
def median(lst):
    """Return median of elements in the list lst."""
    # Sort the list
    sorted_lst = sorted(lst)
    # Calculate the length of the list
    n = len(sorted_lst)
    # Calculate median
    if n % 2 == 1:
        return (sorted_lst[n//2 - 1] + sorted_lst[n//2]) / 2
    else:
        return sorted_lst[n//2]

# Test case 1
median([-10, 4, 6, 1000, 10, 20])
# Test case 2
median([-1, 2, 3, 4, 5, 6, 7, 8, 9])
# Test case 3
median([100, 101, 102])
# Test case 4
median([200, 201, 202])
```
This Python script defines a function called **median** which calculates and returns the median of the elements in a given list. It also comes with a series of test cases to verify the correctness of the function.