Here's the Python code for the function:
```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This function uses an efficient algorithm to check if a number is prime. It begins by initially assuming the low with a counter i = 5, and if the counter exceeds the number and does not result in a divisibility, it increases the counter. This process continues until the values of i multiplied by i exceeds the number, and if the number still is a multiple of a number, it returns false, indicating that the number is not prime. 

The function is self-contained and can be used to efficiently check if a given number is prime in Markdown code blocks.