```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[-1] + lst[::-1]) / 2
    else:
        return lst[n//2]

# Test cases
for case in ['median([3, 1, 2, 4, 5])',
         'median([-10, 4, 6, 1000, 10, 20])']:
    print(f' median({case}) = {median(case)}  -- [ Expected: {case} ]')
```