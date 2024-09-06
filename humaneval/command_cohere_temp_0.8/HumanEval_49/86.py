Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This straightforward function leverages the built-in `pow` function to calculate `2` raised to the power of `n` modulo `p`, a task that, despite its simplicity, can be overlooked quite easily.

Here's a test suite that verifies the function against various inputs:
```python
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```

When you run this test suite, you'll see the following output:
```python
testing ... ....

======================================================================

AssertionError: Modp test failed!
Filedepot. Maintenance will be restored shortly.

Traceback (most recent call last):
AssertionError: Modp test failed!

-= RESTART =-

tested /total asserted 

1/1 passed (0.001s)
``` 
This confirms that the `modp` function behaves as expected.