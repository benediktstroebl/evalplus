```python
def special_factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. This function calculates the `brazilian_factorial` of `n` by iterating through all numbers from 1 to `n` and multiplying them together. This operation is repeated for each number from 1 to `n`, effectively computing the product of all integers from 1 to `n`. This computation is different from the standard factorial, which is defined as `n! = 1 * 2 * 3 * ... * n`. 

The provided code offers an efficient way to compute the `brazilian_factorial`, as it leverages Python's native ability to handle loops and multiplication. As a result, it effortlessly computes the factorial for varying values of `n`. When you require the `brazilian_factorial` for a specific value of `n`, you can invoke the `special_factorial` function and supply that value as an argument.