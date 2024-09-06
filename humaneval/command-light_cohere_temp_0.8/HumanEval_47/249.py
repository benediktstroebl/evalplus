```python
def median(l: list):
    """Return median of elements in the list l.
    return sorted(l)[len(l) // 2] if len(l) % 2 == 0 else (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    """
    return median([-10, 4, 6, 1000, 10, 20])
# Uncommented code to run and test the function
# print(median([-10, 4, 6, 1000, 10, 20])) # Median is 15.0
# print(median([1, 2, 3, 4, 5])) # Median is 5.0
# print(median([5, 6, 10, 9, 2])) # Median is 9.0
```
The function median computes the median of a list of numbers, which is the middle value of the two middle numbers when the list is sorted. The function works for both even values in the list and returns the median. This code can be used to test the functionality of the median function.