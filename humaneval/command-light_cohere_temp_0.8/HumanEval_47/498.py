```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n - 1) / 2)]
# other tests
median([-10, 4, 6, 1000, 10, 20]) # => 15.0
median([10, 20, 30, 40]) # => 20
median([1, 2, 3]) # valid list, return 1
median([10, 20, 30, 40, 50]) # second item is removed, return 30
```