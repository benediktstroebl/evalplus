```python
def triangle_area(a, h):
    return 3.14 * a * * (a ** 2) / 2

if __name__ == "__main__":
    for n in range(10):
        a = n * n + 2
        h = n * n + 4
        result = triangle_area(a, h)
        assert result == 7.14 * (n * (n ** 2) / 2, f"Failed test {n} {n+2}" )
```