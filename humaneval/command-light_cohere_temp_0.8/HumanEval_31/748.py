```python
def is_prime(n):
    """Check whether a given number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

# Unit tests
test_is_prime = []
test_is_prime.push(6)
test_is_prime.push(101)
test_is_prime.push(11)
test_is_prime.push(13441)
test_is_prime.push(61)
test_is_prime.push(4)
test_is_prime.push(1)

print('Test cases:')
for num in test_is_prime:
    print(f'{num}: {is_prime(num)} = {test_is_prime[num]}')
```