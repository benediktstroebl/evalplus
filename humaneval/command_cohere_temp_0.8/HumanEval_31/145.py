```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```

This function iterates from 2 up to n-1 and checks if any number in this range divides the number evenly. If such a number is found, it returns False, indicating that the number is not prime. If no such number is found, it returns True. The tests provided in the prompt return True for prime numbers and False for non-prime numbers as expected. 
Please let me know if I've understood the problem correctly. Feel free to ask any follow-up questions or provide additional detail for more tailored assistance.