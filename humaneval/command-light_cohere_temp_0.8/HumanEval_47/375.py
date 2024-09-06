```python
def median(l: list):
    n = len(l)
    if n % 2 == 1:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]

# Test the function with various input
for _ in range(10):
    test_list = [random.randint(-10, 1000) for _ in range(10)]
    print(median(test_list))
```