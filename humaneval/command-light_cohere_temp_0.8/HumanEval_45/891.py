```python
def triangle_area(a, h):
    return (a * (h + a)) / 2

def test():
    assert triangle_area(5, 3) == 7.5, "Passed test!"
    assert triangle_area(8, 16) == 44, "Failed test"

# Run the function and test it
test()
```