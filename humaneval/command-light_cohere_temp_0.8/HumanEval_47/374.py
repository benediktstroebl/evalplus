```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)::2][0] + lst[n//2][0]) / 2
    else:
        return lst[(n//2)][0]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
```
This function computes the median of the elements in the list lst. The function first checks if the list has an even number of elements. Then, it checks if the list has an even number of elements, then returns the median of the two middle numbers of the list, else, returns the median of the first middle number.