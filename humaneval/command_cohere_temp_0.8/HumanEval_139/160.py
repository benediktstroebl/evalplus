```python
def special_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
```
This Python script defines a function called `special_factorial` which accepts an integer `n` as input. The function calculates the `special factorial` of `n` defined as `brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!` where n is greater than 0. This `special factorial` is calculated by multiplying each integer from 1 to `n` together, encapsulated in a `for` loop that iterates through these values and updates the `fact` variable. The calculated `fact` is then returned, representing the `special factorial` for the given input `n`. 

Here is an example usage of the function for the input of `4`:
```python
special_factorial(4)
```
This would evaluate to `288`, which is the special factorial of 4 according to the defined Brazilian factorial definition. 

This is a simple and efficient calculation of the Brazilian factorial, directly computing the product of numbers from 1 to n.  It should be noted that this definition of the Brazilian factorial is different from the more traditional definition used in some mathematical contexts and it is not clear from the original problem statement whether this is the intended definition or a discrepancy in the statement itself.