```python
def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if a is the product of exactly 3 prime numbers
        prime_factors = []
        for i in range(2, int(a ** 0.5) + 1):
            while a % i == 0:
                prime_factors.append(i)
                a //= i
                if a == 1:
                    break
        if len(prime_factors) == 3 and a == 1:
            return True
    return False
```

The function `is_multiply_prime` checks if `a` is the product of 3 prime numbers by finding all the prime factors of `a` and comparing their count to 3. The loop iterates through all numbers from 2 to the square root of `a` and for each number checking if it's a factor of `a` and if so, it's appended to the `prime_factors` list. Once the loop is completed, if the length of the `prime_factors` list is equal to 3 and `a` equals 1, then return `True`, otherwise, return `False`.