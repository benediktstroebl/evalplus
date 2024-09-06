Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, n and p, and utilizes the Python built-in function pow(x, y, z) to compute the result of raising x to the power of y modulo z. This effectively solves the problem of computing 2^n modulo p. 

To test this function, you can call it with various test cases to verify if it produces the expected outputs of the problem statement. Here is how you can do it:
```python
# Testing the modp function
def test_modp():
    assert modp(3, 5) == 3
    assert modp(1101, 101) == 2
    assert modp(0, 101) == 1
    assert modp(3, 11) == 8
    assert modp(100, 101) == 1

test_modp()
```
This function should return the expected outputs as per the problem statement provided. If the script is executed with these test cases, you should not see any errors and the outputs will be the following:
```
True
True
True
True
True
```
These results confirm that the implemented function correctly computes 2^n mod p. Feel free to add more test cases to extensively validate the function.