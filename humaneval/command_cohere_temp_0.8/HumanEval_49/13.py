Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`. It utilizes the `pow()` function to compute `2` raised to the power of `n` modulo `p`, adhering to the problem statement. The "modp.py" file must be included in the same directory as the script for this code to function properly. This file contains the definitions for the `pow()` function. 
The following code is an example of how to test this function:
```python
def test_modp():
    assert modp(0, 101) == 1
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1
```

The test code will generate specific scenarios and confirm that the function's output matches the expected outcome.

You may simply incorporate this function into your code and customize it to meet your unique requirements because it is a stand-alone solution.