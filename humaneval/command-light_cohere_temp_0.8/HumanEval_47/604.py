```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n // 2) - 1] + lst[n // 2]) / 2
    else:
        return lst[(n // 2)]

# Test cases
for i in range(0, 10):
    test_lst = [i, i+1, i*2, 10, i*3]
    print(median(test_lst), end=' ')
```