Here's a self-contained Python function that checks if a given number is prime: 

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True
``` 

This function uses a 'for' loop to check divisibility by numbers up to the square root of the number. It returns 'True' if the number is prime and 'False' otherwise. 

This function is self-contained and can be easily incorporated into larger scripts or used directly as-is.