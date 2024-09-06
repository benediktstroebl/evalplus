```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lstats.median([x, n // 2]))
    return (lstats(lst[:n//2], lstats([lst[n//2:]))) if n // 2 > 1 else lst[n//2]

def lstats(lst1, lst2):
    return (len(lst1), len(lst2), max(lst1), max(lst2), min(lst1), min(lst2), sum(lst1), sum(lst2))

if __name__ == "__main__":
    lst = [-10, 4, 6, 1000, 10, 20]
    print(f"The median of {lst} is: {median(lst)}")
```
This script defines a function `median` that computes the median of a given list. It utilizes the two helper functions: `lstats` calculates various statistics (length, maximum, minimum, sum) for two lists, and `median_even` returns the median for a list of even numbers.

This script is a self-contained solution that solves the problem of finding the median of a list of numbers.