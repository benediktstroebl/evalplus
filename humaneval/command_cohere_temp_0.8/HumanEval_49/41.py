Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, n and p, and utilizes the Python built-in function pow(x, y, z) to compute the result of raising x to the power of y modulo z. This is achieved as follows:
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
This solution is concise and straightforward, leveraging Python's built-in functionalities to solve the problem. 
If you would like to explore alternative approaches or provide any further details that you are working on, feel free to continue the conversation!