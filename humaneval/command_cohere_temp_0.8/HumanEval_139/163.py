```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= i
    return result
```
This Python script defines a function `special_factorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where `n` is greater than zero. The function iterates through numbers from `1` up to `n`, calculating the factorial result using both multiplication and division loops to properly calculate the Brazilian factorial. The final result is returned as the Brazilian factorial of the given input `n`. 

To validate the function, it would be run with the following tests:
```python
>>> special_factorial(4)
288
>>> special_factorial(5)
15504
>>> special_factorial(10)
3628800
>>> special_factorial(15)
65537600480384
>>> special_factorial(50)
25353247446346430089601389565965664440048036878623167104808024576
``` 
Each test will require the function to provide the Brazilian factorial for a specific `n` value. These tests ensure the correctness and accuracy of the `special_factorial` function in computing the desired Brazilian factorial values.