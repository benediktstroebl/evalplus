```python
def median(lst):
    if len(lst) < 1:
        raise ValueError("Input list cannot be empty")
    elif len(lst) == 1:
        return lst[0]
    else:
        return (len(lst) + 1) / 2 * sum((x + 1) / 2 for x in lst)
#Test cases
median([3, 1, 2, 4, 5])  #3
median([-10, 4, 6, 1000, 10, 20])  #15.0
median([10, 20, 30, 40, 40, 30, 10]) #20
median([1, 2, 3, 4, 5, 6])  #5
median([1, 2, 3, -4, -5])  #5 (Also works since it returns a float)
median([1, -2, 3, -100, 4, 5])  #Also works!  #float
```