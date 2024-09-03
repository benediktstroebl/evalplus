```python
def is_simple_power(x, n):
    return x ** n == x
def test():
    assert is_simple_power(1, 4)
    assert is_simple_power(2, 2)
    assert is_simple_power(8, 2)
    assert is_simple_power(3, 2) == False
    assert is_simple_power(3, 1) == False
    assert is_simple_power(5, 3) == False

# You can add more tests to pass additional checks if needed.
```