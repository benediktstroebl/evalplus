Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which takes in two integers n and p and returns 2^n modulo p. This is accomplished by using the built-in Python function pow which returns x to the y power modulo m. 

To test this function, you can call it with different input values to verify that it returns the expected outputs, as demonstrated in the given example. You can also adapt the given tests in the markdown code block to check the functionality of the provided solution. Here is an example:
```python
>>> modp(3, 5)
3
>>> modp(1101, 101)
2
>>> modp(0, 101)
1
>>> modp(3, 11)
8
>>> modp(100, 101)
1
```
This shows that the provided function works as expected, returning the values from the original prompt.