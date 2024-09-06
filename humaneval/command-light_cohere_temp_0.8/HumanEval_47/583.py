```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[-1] + l[0]) / 2
    else:
        return l[int((n - 1) / 2)]

# Test cases
for i in range(10):
    test_lst = [i, i+1]
    print(median(test_lst), end=" ")
```