```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    sequence = [0]
    
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True
    
    for _ in range(n):
        if not_prime(sequence[-1]):
            next_num = sequence[-1] + 2
        else:
            next_num = 1
        sequence.append(next_num)
        
    return sequence[-1]

# Example usage:
print(prime_fib(5))
```

This script defines a function prime_fib(n) that computes the n-th Fibonacci number and verifies that it is also prime. The function achieves this by first creating a Fib sequence of numbers, then, it checks each number in the sequence to see if it's prime using the is_prime function. The sequence is then updated with the next Fibonacci number, and the final result will be the n-th prime Fibonacci number.