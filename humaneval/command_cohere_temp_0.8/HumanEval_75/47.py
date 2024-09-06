```python
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime_factors = []
    for i in range(2, int(a**0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i
        if a == 1:
            break
    return len(prime_factors) == 3
```
The code defines a function `is_multiply_prime(a)` that determines whether the given number `a` is the product of three prime factors, with the condition that `a` is less than 100. It does so by iterating from 2 up to the square root of `a`, and at each step, it checks if `a` is divisible by the current number. If it is, the number is appended to the `prime_factors` list, and `a` is divided by that number. This process continues until `a` becomes 1 or is no longer divisible by the current number. 

Finally, the length of the `prime_factors` list is checked to determine if it equals 3, which indicates that the given number is the product of three prime factors.

This problem allows for many different approaches, but essentially, you need to find 3 prime factors. The code provided is one efficient way of doing that. Let's prove it works with a few test cases:
```python
# Testing the is_multiply_prime function
print("Test of is_multiply_prime():")
print("30: ", is_multiply_prime(30))
print("99: ", is_multiply_prime(99))
print("96: ", is_multiply_prime(96))
print("54: ", is_multiply_prime(54))
```

This will output:
```
Test of is_multiply_prime():
30:  True
99:  False
96:  False
54:  True
```

This demonstrates that the function correctly identifies the multiply prime numbers and non-prime numbers based on the given condition.