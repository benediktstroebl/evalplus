```python
def f(n):
    return [x for x in range(1, n + 1)]

# Test the function
for i in range(10):
    assert f(i) == [1, 2, 6, 24, 15, 10, 50, 100, 375, 635, 2150]
```