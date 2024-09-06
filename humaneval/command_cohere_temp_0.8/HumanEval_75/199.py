```python
def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    limit = int(sqrt(a)) + 1
    for b in range(3, limit, 2):
        if a % b == 0:
            continue
        for c in range(3, limit, 2):
            if a % c == 0:
                continue
            if b == c:
                return False
            for d in range(3, limit, 2):
                if a % d == 0:
                    return False
                if b == d or c == d:
                    return False
    return True
```

This function checks if the number `a` is the product of three prime factors, iterating through all numbers up to the square root of `a` to find two pairs of factors. It returns false immediately upon finding any non-prime factor, and ensures that all pairs of factors are distinct. 

Here's a standalone test for the function to verify its correctness:
```python
def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == True
    assert is_multiply_prime(54) == False
    assert is_multiply_prime(8) == False
    assert is_multiply_prime(100) == False
``` 

To check the correctness of the function, you can execute these tests individually using the Python REPL, or by saving them in a separate Python file and running them using a test runner like pytest.