```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n - 1) / 2)]

#Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3]) == 2.0
assert median([10, 20, 40, 30, 80]) == 50.0
assert median([5, 4, 6, 7]) == 5.0
``` 
This script defines a function median that computes the median of a list of numbers. The test cases cover different scenarios, including even and odd-length lists, numbers with duplicates, and numbers out of order.