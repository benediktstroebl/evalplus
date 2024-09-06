```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

if __name__ == "__main__":
    for i in range(10):
        a = 2 + i
        h = 3 + i
        result = triangle_area(a, h)
        assert result == 3.14159 * (a** 2 * h),
        print("Test passed!")
```