Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It utilizes the `pow` function to compute `2` raised to the power of `n` modulo `p`, adhering to the corresponding warning about numerics.

Here's an illustrative test suite showcasing the function's behavior:
```python
def test_modp():
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```
This test suite contains several test cases, each of which asserts that the output of the `modp` function is as expected. If the function is correct, all tests should pass without raising an exception.