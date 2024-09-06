```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l [-1] + l[-2]) / 2
    else:
        return l[-n // 2]
# test cases
median([3, 1, 2, 4, 5]) #3
median([-10, 4, 6, 1000, 10, 20]) #15
median([-5, -3, -10, -20, -25]) #15
median([2, 7, 3, 4, 5]) #3
median([10, 20, 30, 40]) #10
```