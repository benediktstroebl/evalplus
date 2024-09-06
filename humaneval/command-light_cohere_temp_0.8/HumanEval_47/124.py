```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for _ in range(50):
    test_lst = [random.randint(-1000, 1000) for _ in range(5)]
    assert median(test_lst) == int((test_lst[2] + test_lst[3]) / 2)
```