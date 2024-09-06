```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n // 2] + l[n // 2 - 1]) / 2
    else:
        return l[n // 2]

# Test the function
for _ in range(25):
    test_lst = [i % 1000 for i in range(1, 1001)]
    assert median(test_lst) == int(test_lst[500] if len(test_lst) % 2 == 0 else test_lst[250])
```