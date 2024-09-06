Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs and utilizes the Python `pow` function with the second argument modulo the third argument to calculate 2^n modulo p, which is the equivalent of the expression return 2 ** (n % p). This equation simplifies the code while retaining the same desired functionality. 

To follow the provided markdown code block format, here is an example usage case for this function:
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
This shows the expected behavior of the function, returning 3, 2, 1, 8, and 1 for the provided test cases, respectively.