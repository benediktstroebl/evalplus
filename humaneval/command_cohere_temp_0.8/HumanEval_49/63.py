Here's a Python script with a self-contained function that solves the problem:
```python
def modp(n, p):
    return pow(2, n, p)
```
This function defines the modp function which takes in two integers n and p and returns 2 raised to the power of n modulo p. This is accomplished by using the built-in function pow which handles the exponentiation and modulus operations for us, relieving us from manually implementing the algorithm. 

This solution should produce the following results:
```
> modp(3, 5)
3
> modp(1101, 101)
2
> modp(0, 101)
1
> modp(3, 11)
8
> modp(100, 101)
1
```
These outcomes align with the problem's expectations, demonstrating the function's correctness.

This solution is efficient and utilizes Python's built-in features for modular exponentiation, making it a reliable choice.

This approach allows us to easily handle complex computations with large numbers and moduli, simplifying the process and enhancing the performance of the solution.