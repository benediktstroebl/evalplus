Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function which takes in two integers `n` and `p` and returns `2` raised to the power of `n` modulo `p`. This is accomplished by using the built-in Python function `pow` with the modulo operator to calculate the result. 

To use this script, you can call the `modp` function with any valid input as shown in the example below:
```python
print(modp(3, 5)) # 3
print(modp(1101, 101)) # 2
print(modp(0, 101)) # 1
print(modp(3, 11)) # 8
print(modp(100, 101)) # 1
```
This script provides an efficient solution and passes the given tests since the built-in Python function `pow` is designed to handle such operations while maintaining efficiency.