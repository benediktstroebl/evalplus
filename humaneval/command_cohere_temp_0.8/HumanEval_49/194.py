Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as inputs and utilizes the Python built-in function `pow` to calculate `2` raised to the power of `n` modulo `p`. 
It then returns the resulting value. 

Here is an example usage of the function:
```python
n = 3
p = 5
print(modp(n, p)) 
```
This will output:
```
3
```

This showcases how the function effectively computes and returns the solution, as defined by the problem statement. 

This function is self-contained, easy to understand, and follows Python's PEP 8 style guide. 

It can be easily executed and adapted to solve similar problems that involve modular arithmetic.