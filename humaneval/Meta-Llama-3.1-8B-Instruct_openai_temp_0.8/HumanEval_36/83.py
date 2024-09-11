```python
def count_sevens(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the range of numbers to check.

    Returns:
    int: The count of digit 7 in numbers less than n that are divisible by 11 or 13.
    """
    count = 0
    for i in range(2, n):  # Start from 2 since we're looking for multiples of 11 and 13
        if i % 11 == 0 or i % 13 == 0:
            str_i = str(i)
            count += str_i.count('7')  # Increment count for each occurrence of '7' in str_i
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
    n (int): The upper limit for the range of numbers to check.

    Returns:
    int: The count of digit 7 in numbers less than n that are divisible by 11 or 13.
    """
    return count_sevens(n)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```

In this script, we separate the counting logic from the main `fizz_buzz` function for better readability and maintainability. The `count_sevens` function counts the occurrences of the digit 7 in numbers divisible by 11 or 13, and the `fizz_buzz` function simply calls `count_sevens` with its argument `n`.