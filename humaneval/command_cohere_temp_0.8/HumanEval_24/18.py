```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n + 1):
        if n % i == 0:
            return i
```
The function `largest_divisor(n)` takes a number `n` as input and iterates through all numbers from 1 to `n` (inclusive). During each iteration, it checks if the current number `i` can divide `n` evenly. This is done by using the modulo operator '%' which returns the remainder of the division of the first number by the second one. In this case, if the remainder is 0, it means that `i` is a divisor of `n`, and therefore it is the largest divisor found so far, as the search continues the value is kept in the 'i' variable and is returned once the loop is finished.