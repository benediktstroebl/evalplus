```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[n//2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 3.0
assert median([10, 11, 12, 13, 14]) == 13.0
assert median([10, 20, 30, 40, 30]) == 30.0
```
The median function calculates the median of the elements in the list lst. It handles the cases where the list has an even or odd number of elements, it returns the median of the first and last element of the list, respectively. If the list has an single element, it returns that element.