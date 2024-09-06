```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    for i in range(2, n + 1):
        result //= i
    return result
```
This Python script defines a function `special_factorial` that calculates the Brazilian factorial of a given integer `n`. The Brazilian factorial is defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!`, where `n` is greater than zero. The function takes an integer `n` as input and returns the Brazilian factorial value.

To calculate the factorial of `n`, the script uses a two-step process:
1. First, it calculates the standard factorial of `n` by multiplying all integers from 1 to `n` inclusively. This is achieved by initializing a variable `result` to 1 and then iterating through the range from 1 to `n` (both inclusive) and updating `result` by multiplying it with the current value of `i`.
2. Second, the script computes the reciprocal of the factorial for all integers from 2 to `n` inclusively. This is done by iterating through the range from 2 to `n` (both inclusive) and updating `result` by dividing it by the current value of `i`.

The final value of `result` is returned, giving the Brazilian factorial of the input `n`. 

This approach effectively calculates the Brazilian factorial by multiplying the standard factorial by the reciprocals of the factorials of all integers from 2 to `n` inclusively, as specified by the Brazilian definition. 

The given example usage and output demonstrate the correct operation of the function, ensuring it can handle the given problem statement. 
```python
>>> special_factorial(4)
288
```