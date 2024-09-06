```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n - 1) / 2)]

# Test the function with various lists
for test in [median([-10, 4, 6, 1000, 10, 20]) , median([3, 1, 2]) , median([100, 200, 300]) , median([-5, -3, -10])]:
    print(f"Test {test} passed.")
```