```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for i in range(10):
    test_lst = [i, i*2+1, i*3+2]
    assert median(test_lst) == i*3+1
```