```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n - 1) / 2)]

# Test cases
for _ in range(25):
    test_list = [random.randint(-1000, 1000) for _ in range(5)]
    assert median(test_list) == int((len(test_list) + 1) / 2)
```