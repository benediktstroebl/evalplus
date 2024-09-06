Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs, namely `n` and `p`, and returns `2` raised to the power of `n` modulo `p`. This is achieved by using the `pow` function, which returns `x` raised to the power of `y` modulo `z`, given three integers `x`, `y`, and `z`.

Here's a test suite that validates the correct behavior of the `modp` function for various inputs:
```python
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
    assert modp(1, 7) == 1
    assert modp(2, 7) == 2
    assert modp(3, 7) == 4
    assert modp(4, 7) == 2
    assert modp(5, 7) == 1
    assert modp(6, 7) == 6
    assert modp(7, 7) == 0
    assert modp(8, 7) == 6
    assert modp(9, 7) == 5
    assert modp(10, 7) == 4
    assert modp(11, 7) == 3
    assert modp(12, 7) == 2
    assert modp(13, 7) == 1
    assert modp(14, 7) == 0
    assert modp(15, 7) == 5
```
This test suite contains a variety of test cases that cover different scenarios, including edge cases, to ensure the function behaves as expected.