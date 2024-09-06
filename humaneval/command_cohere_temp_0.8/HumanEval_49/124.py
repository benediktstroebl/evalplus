Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function accepts two integers as parameters, namely `n` and `p`, and computes the result of 2 raised to the power of `n` and then takes the modulo of the result with `p`. This is achieved through Python's built-in function `pow()`, which computing x to the power of y modulo z where x, y, and z are provided integers. In this case, it computes 2 to the power of `n` modulo `p`. 

Here's an example usage of the function:
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
The example tests match the specification's example tests and demonstrate the function's behavior when provided with different inputs. 
It's essential to recognize that the original problem statement cautions about the potential for numerical issues when the argument computations are close to the modulo limit. Despite the lack of such warnings in the provided Python solution, it is still a good practice to be aware of these potential issues when solving the problem in a practical context.