```python
def median(lst):
    # Sort the list
    lst.sort()
    
    # if len(lst) % 2 == 0:
        return (lst[len(lst) // 2][0] + lst[len(lst) // 2][1]) / 2
    # else:
        return lst[len(lst) // 2][0]

# Test the function
assert(median([3, 1, 2, 4, 5])) == 3
assert(median([-10, 4, 6, 1000, 10, 20])) == 15)
assert(median([-5, -5, -5, -5, -5])) == -5)
assert(median([10, 10, 10])) == 10)
```