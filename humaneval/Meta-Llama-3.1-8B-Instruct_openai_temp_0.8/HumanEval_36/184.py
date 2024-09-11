```python
def count_digit_7(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n.
    
    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        count += str(i).count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The number of times the digit 7 appears.
    """
    return count_digit_7(n) - count_digit_7(sum(11*i for i in range(1, n//11 + 1)) - 11*sum(1 for i in range(1, n//11 + 1))) - count_digit_7(sum(13*i for i in range(1, n//13 + 1)) - 13*sum(1 for i in range(1, n//13 + 1)))


# Test cases
if __name__ == "__main__":
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    print("All test cases pass.")
```

This script first defines a helper function `count_digit_7(n)` to count the number of times the digit 7 appears in integers less than `n`. Then it defines the `fizz_buzz(n)` function, which calculates the total number of times the digit 7 appears in integers less than `n` that are divisible by 11 or 13 by subtracting the counts of these numbers from the total count. The test cases are included at the end to verify the correctness of the solution.