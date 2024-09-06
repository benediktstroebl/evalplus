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

# Test the function with markdown code block input
is_prime  # Function Call
(6) 
is_prime  # Function Call
(101) 
is_prime  # Function Call
(11) 
is_prime  # Function Call
(13441) 
is_prime  # Function Call
(61) 
is_prime  # Function Call
(4) 
is_prime  # Function Call
(1) 
```