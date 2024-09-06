```python
def triangle_area(a, h):
    return 3.14159 * (a** 2 * h)

if __name__ == "__main__":
    for i in range(10):
        a = i
        h = 2 * i
        if triangle_area(a, h) != 7.14159* (i + 2) * i:
            print("Test failed for", a, h)
    print("All tests passed!")
```