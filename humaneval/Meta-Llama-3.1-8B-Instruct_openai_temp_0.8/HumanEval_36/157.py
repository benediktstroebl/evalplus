```python
def count_sevens(n: int) -> int:
    """
    Helper function to count the occurrences of the digit 7 in a number.
    
    Args:
    num (int): The number to check.
    
    Returns:
    int: The number of times the digit 7 appears in num.
    """
    return str(num).count('7')


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit.
    
    Returns:
    int: The total count of digit 7 in numbers less than n divisible by 11 or 13.
    """
    return sum(count_sevens(i) for i in range(n) if i % 11 == 0 or i % 13 == 0)


# Test cases
if __name__ == "__main__":
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```

This script provides a concise solution to the problem. The `count_sevens` function counts the occurrences of the digit 7 in a given number by converting the number to a string and using the `count` method. The `fizz_buzz` function sums up the counts of the digit 7 for all numbers less than the given limit that are divisible by 11 or 13. The test cases verify the correctness of the solution.