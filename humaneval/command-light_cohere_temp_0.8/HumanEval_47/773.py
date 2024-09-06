```python
def median(l: list):
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
for _ in range(50):
    test_list = [random.randint(-1000, 1000) for _ in range(5)]
    assert median(test_list) == int((test_list[2] + test_list[3]) / 2)
```