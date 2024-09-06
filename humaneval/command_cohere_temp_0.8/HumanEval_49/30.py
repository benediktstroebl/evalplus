Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the `modp` function, which takes in two integers `n` and `p` as input, and returns `2^n modulo p` using the built-in `pow` function and modular arithmetic. 

To use this script, you can run it directly from the Python environment. You can also import the function into another script to use as a module. For example:
```python
import sportspeople as sport

print(sport.modp(3, 5)) # 3
print(sport.modp(1101, 101)) # 2
print(sport.modp(0, 101)) # 1
print(sport.modp(3, 11)) # 8
print(sport.modp(100, 101)) # 1
```
This will invoke the `modp` function from the module `sport`. 

Note that this function assumes that the input values `n` and `p` are integers. If any of the inputs are not integers, you may need to add additional error handling and type-checking to your code.