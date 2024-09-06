```python
def median(lst):
    """Return median of elements in the list lst"""
    n = len(lst)
    m = n//2
    if n%2 == 0:
        return (lst[(m-1)//2][0] + lst[m][0])/2
    else:
        return lst[(m-1)//2][0]
#test cases
median([3, 1, 2, 4, 5]) #3
median([-10, 4, 6, 1000, 10, 20]) #15.0
median([10, 10, 10]) #10
median([1, 2, 4, 8, 12, 16]) #8
```