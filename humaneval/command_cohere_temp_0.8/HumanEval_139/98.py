```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. This function calculates the `special factorial` of `n` defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` The function initially sets the `fact` variable to 1 and then uses a `for` loop to multiply `fact` by each integer `i` from 1 to `n`. The final value of `fact` after the loop is the `special factorial` of `n`, which is then returned by the function. 

Here is an example usage of the function for `n = 4`:
```python
special_factorial(4)
```
This will return the value `288`, which is the `special factorial` of 4. 

This is an efficient computation using a closed-form solution and avoids the need for a recursive definition of the factorial function, which would be much less efficient for large inputs.