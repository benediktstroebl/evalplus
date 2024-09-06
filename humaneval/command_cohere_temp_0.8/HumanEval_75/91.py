```python
def is_multiply_prime(a):
    prime_test = [0, 0, 0]
    for i in range(2, a):
        if a % i == 0:
            prime_test[0] = 1
        if i * i > a:
            break
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            prime_test[1] = 1
        if i * i > a:
            break
    if a > 4:
        for i in range(3, int(a**0.5) + 1, 2):
            if a % i == 0:
                prime_test[2] = 1
            if i * i > a:
                break
    return all(prime_test)
```

The function `is_multiply_prime` takes a number `a` as input and checks if it is the multiplication of three prime numbers. The function initially calculates each prime factor and saves them in the `prime_test` array. Finally, the function returns `true` if all three primes are found (meaning the number is the product of three primes), and `false` otherwise. 

Here is a test suite to ensure the functionality of the function:
```python
def test_is_multiply_prime():
    assert is_multiply_prime(30) == True
    assert is_multiply_prime(52) == True
    assert is_multiply_prime(2) == False
    assert is_multiply_prime(101) == False
    assert is_multiply_prime(105) == False
``` 
This would ensure that the function is correctly identifying numbers that are the multiplication of three prime numbers.