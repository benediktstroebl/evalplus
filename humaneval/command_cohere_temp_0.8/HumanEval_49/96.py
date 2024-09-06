```python
def modp(n, p):
    return (1 << n) % p
```

This function takes two arguments, `n` and `p`, and returns the result of performing the bitwise operation `1 << n` (which is equivalent to `2 ** n`) and then taking the result modulo `p`. This operation is useful for efficiently calculating the result of raising 2 to a given power and taking the result modulo a given number, which can be important in various mathematical and computational scenarios. 

Here is a test suite that can be used to validate the function:
```python
def test_modp():
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```

This test suite contains several test cases, and when run, they validate that the `modp` function behaves as expected. By running these tests, you can confirm that the function works correctly for different inputs.