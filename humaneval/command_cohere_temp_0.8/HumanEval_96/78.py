```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    prime_numbers = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            prime_numbers.append(i)
            count += 1
            if count == n:
                break
    return prime_numbers
```

The `count_up_to()` function initializes a counter `count` and an empty array `prime_numbers`. It then iterates through integers from 2 up to `n`, checking each with the `is_prime()` function. When it finds a prime number less than `n`, it increments `count`, adds the prime number to `prime_numbers`, and if `count` equals the desired value `n`, it breaks out of the loop to stop generating more primes than desired. The function returns `prime_numbers`, an array of the first `n` prime numbers less than `n`. 

To ensure that the implementation works correctly, it is recommended to verify it with tests. Here are some test cases to get started:
```python
# Test cases for the is_prime function
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False

# Test cases for the count_up_to function
def test_count_up_to():
    assert count_up_to(5)[0] == 2
    assert count_up_to(5)[1] == 3
    assert count_up_to(11)[:4] == [2, 3, 5, 7]
    assert count_up_to(20)[:7] == [2, 3, 5, 7, 11, 13, 17]
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(18)[:6] == [2, 3, 5, 7, 11, 13]
```

To run these test cases, create a separate file with the tests or add them to the bottom of the script, inside the `__main__` clause. Then, run the script, and the `assert` statements will check that the prime number functions work as expected. If there are no assertions, then all tests pass. 

This approach covers different scenarios that the problem statement intends to tackle. However, if you'd like to further expand the solution or explore more test cases, let me know!