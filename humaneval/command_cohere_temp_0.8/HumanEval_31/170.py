```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function iterates from 2 up to n-1 and checks if any of these values evenly divide the number. If so, it returns false, while any other result is considered prime. 
If n=1, the function returns false, as the unit test suggests. Additionally, it handles the special case where n is less than 2, in which it returns false as well. 
Overall, the function's implementation is efficient and adheres to Python's PEP 8 style guide, making it clean and easy to read. It successfully solves the problem of checking for prime numbers while maintaining a concise and self-contained implementation.