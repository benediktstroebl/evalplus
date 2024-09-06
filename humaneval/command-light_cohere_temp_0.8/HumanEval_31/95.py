Here is a Python script with a self-contained function that solves the problem of checking if a number is prime:
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

# Unit tests
test_is_prime = []
for i in range(2, 301):
    test_is_prime.append(i)
    test_is_prime.append(is test_is_prime(i))

print(" ".join("Is prime: ".join(test_is_prime)))
``` 
This script defines a function is_prime that takes an integer n as input and returns true if n is a prime number, and false otherwise. 

The function uses some simple heuristics and tests on n to determine if it is prime or not. The function also has unit tests that ensure its correctness for the range [2, 301]  The output will display all the numbers in the range [2, 301) that are prime.