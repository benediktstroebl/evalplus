Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function defines a logical and efficient algorithm to determine whether a given number n is prime. It begins by handling the special case of n being less than 2, ensuring that attention is paid to nuances and edge cases. Subsequently, the function executes a loop from 2 to n's square root, examining all potential divisors. Finally, the function returns False if any divisors are found, and True if none are, thus indicating whether the number is prime. 

This approach balances computational efficiency and algorithmic clarity, giving a nuanced and adaptable solution.