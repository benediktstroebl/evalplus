```python
def special_factorial(n):
    """
    Brazilian factorial is defined as:
        brazilian_factorial(n) = n!. * (n-1)! * ... * 1
    where n > 0

    Returns:
        int: Special factorial number
    """
    return n*(n*special_factorial(n-1))

if __name__ == "__main__":
    print(special_factorial(4))
    print(special_factorial(0))
    print(special_factorial(5))
    print(special_factorial(6))
    print(special_factorial(7))
    print(special_factorial(8))
    print(special_factorial(9))
    print(special_factorial(10))
```
This code defines a function `special_factorial` that computes the Brazilian factorial. It uses recursion, following the definition of the factorial function. The tests are at the main function to ensure that the function is working correctly.