```python
def count_sevens(num: int) -> int:
    """
    Count the number of times the digit 7 appears in the representation of a number.

    Args:
    num (int): The number to count the digit 7 in.

    Returns:
    int: The number of times the digit 7 appears in the representation of the number.
    """
    return str(num).count('7')


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the integers to check.

    Returns:
    int: The count of integers less than n which are divisible by 11 or 13 and contain the digit 7.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_sevens(i)
    return count


# Example usage
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```

This script defines two helper functions: `count_sevens` to count the occurrences of the digit 7 in a number, and `fizz_buzz` to count the numbers that meet the original condition. The `fizz_buzz` function iterates over integers less than the given number and checks if they are divisible by 11 or 13. If they are, it adds the count of digit 7 occurrences to the total count. The script also includes example usage in the `if __name__ == "__main__":` block.