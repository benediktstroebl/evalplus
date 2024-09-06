```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the problem statement by determining a number's primality, incorporating edge cases like 1 and composite numbers. It iterates from 2 up to the square root of the number, checking for divisibility. If none is found, the number is prime; otherwise, it's composite. 

Feel free to experiment with other problem-solving approaches or add more test cases to further validate the function's behavior. Let me know if you'd like to discuss any particular aspect or explore alternative solutions!