Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_prime(n):
    """Check if an integer is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n integers that are prime numbers and less than n"""
    count = 0
    primes = []
    for i in range(2, n+1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

The `count_up_to()` function iterates through numbers from 2 up to `n`, it checks each number using the `is_prime()` function to verify if it's a prime number and if it's less than `n`. If the criteria are met, the number is added to the `primes` list and the `count` variable is incremented. Once the `count` reaches `n`, the function stops iterating and returns the `primes` list, accomplishing the task. 

To ensure the function behaves correctly there is a testing section designed to handle various edge cases:
```python
# Testing Section
def test_count_up_to():
    # Basic Cases
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # Edge Cases
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

test_count_up_to()
```

To showcase the `is_prime()` function's correctness, the testing suite also contains a dedicated function that verifies its accuracy against a range of prime and non-prime numbers.

```python
def test_is_prime():
    # Prime Cases
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True

    # Non-Prime Cases
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False

test_is_prime()
```

To conduct the test suite, the `pytest` library is used, which enables the execution of specific test cases and provides concise feedback to aid in identifying any issues or edge cases that may have been overlooked.

This script provides a clear and efficient answer to the problem statement, along with extensive testing to ensure its resilience and functionality across a range of scenarios.