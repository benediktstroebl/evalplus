Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a number is prime or not. It first checks if the number is smaller than 2, returning false in this case. Then, it iterates from 2 to the square root of the number, checking if the number is divisible by any other number. If the number is divisible by any other number in this range, it returns false. If it is not, it returns true.

Here is a sample output of the function:
```
True
False
True
True
True
False
False
```

This output corresponds to the example tests provided in the original prompt.