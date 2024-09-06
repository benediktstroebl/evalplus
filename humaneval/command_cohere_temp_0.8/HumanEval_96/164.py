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
    """Return an array of the first n prime numbers less than n"""
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

The `is_prime` function checks if a given number is prime or not. Then the `count_up_to` function generates a list of the first `n` prime numbers less than `n` by using the `is_prime` function to check if each number is prime, and if so, adding it to the list `primes` and incrementing the count `count`. The loop continues until `count` reaches `n`, at which point it breaks to prevent further primes from being added to the list.

Here is a test suite to ensure the functionality of the code:
```python
def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(0) == False
    assert is_prime(1) == False

def test_count_up_to():
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(0) == []
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(1) == []
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
```

The first test checks the `is_prime` function for multiple cases. The second test suite checks the `count_up_to` function for multiple cases. 

These tests can be run with the following command:
```python
python test_count_up_to.py
```

This will run the test suite and output the results, ensuring that the code behaves as expected.