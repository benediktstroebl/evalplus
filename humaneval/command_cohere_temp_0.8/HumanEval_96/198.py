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
    for num in range(2, n+1):
        if is_prime(num) and num < n:
            prime_numbers.append(num)
            count += 1
            if count == n:
                break
    return prime_numbers
```

This script defines a function `count_up_to()` that takes an integer `n` as input and returns an array of the first `n` prime numbers less than `n`. 

The `is_prime()` function is used to check if a number is prime. It uses a simple optimization by checking only up to the square root of the number, since all larger factors can be expressed as a product of smaller factors that are smaller than the square root. The `count_up_to()` function iterates through numbers from 2 up to `n`, adding prime numbers to the `prime_numbers` list until the list has `n` elements, fulfilling the requirements of the problem.

Here is a simple test suite to verify the correctness of the `is_prime()` function

```python
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
```

And here is a test suite for the `count_up_to()` function: 

```python
def test_count_up_to():
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]
```

You can verify the test suites themselves for correctness, as well as the coverage to make sure that the code covers all edge cases and handles them correctly. Feel free to modify the test suites accordingly if needed.