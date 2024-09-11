```python
def count_digit_seven(num: int) -> int:
    """
    Count the number of times the digit 7 appears in a given number.

    Args:
    num (int): The number to count digit 7 in.

    Returns:
    int: The number of times digit 7 appears in num.
    """
    count = 0
    for digit in str(num):
        if digit == '7':
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper bound.

    Returns:
    int: The number of times digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_seven(i)
    return count


# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```
This script defines two functions: `count_digit_seven` and `fizz_buzz`. The `count_digit_seven` function counts the number of times the digit 7 appears in a given number. The `fizz_buzz` function uses `count_digit_seven` to count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The test cases are included at the end to demonstrate the function's behavior.