```python
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    res = []
    for i in range(2, n):
        if is_prime(i) and i < n:
            res.append(i)
    return res

def test_count_up_to():
    assert count_up_to(0) == []
    assert count_up_to(1) == []
    assert count_up_to(5) == [2, 3]
    assert count_up_to(11) == [2, 3, 5, 7]
    assert count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert count_up_to(18) == [2, 3, 5, 7, 11, 13, 17]

if __name__ == "__main__":
    test_count_up_to()
```

The script comes with a `is_prime` function that checks if a given number is prime. It iterates from 2 to `sqrt(n)` and checks if n is divisible by any number in this range, if it is, it returns `False`. The `count_up_to` function uses the `is_prime` function to solve the problem, it iterates from 2 to n and appends the prime numbers to the res list. Finally, the `test_count_up_to` function provides test cases for the `count_up_to` function. When the script is run, it executes the `test_count_up_to` function. 

Note: The `is_prime` function is not optimized, it may not be efficient for larger numbers, but it would work for the ranges specified in the task.