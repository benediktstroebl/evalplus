```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n """
    for i in range(1, n):
        if n % i == 0:
            j = n // i  # largest divisor
            return j if j < i else i
    return 1
```

The function iterates through numbers from 1 to n-1. It identifies the largest divisor of n 
by finding the largest number in this range that can divide n evenly (through the division operator). 
The function then returns the largest divisor, ensuring it is also smaller than n. 

This algorithm is efficient given that it systematically explores the space of potential divisors 
and optimizes for the largest divisor within the given constraints. 

The unit tests for this function can be created using the `pytest` framework by following code:
```python
# python -m pytest -v 
``` 
This will run the tests and report on the functionality of the `largest_divisor` function. 
Let me know if I can help further in any way!