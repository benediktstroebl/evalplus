```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l(lst)[n//2 - 1] + lst[n//2]) / 2
    else:
        return l(lst)[n//2]

def lst():
    return [-10, 4, 6, 1000, 10, 20]

if median(lst()) == 15.0:
    print("Passed tests")
else:
    print("Failed tests")
```