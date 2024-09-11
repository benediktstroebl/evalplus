```python
def count_digit_7(n: int) -> int:
    """Helper function to count the number of times the digit 7 appears in a number."""
    count = 0
    for digit in str(n):
        if digit == '7':
            count += 1
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n 
    which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i)
    return count


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # 0
    print(fizz_buzz(78))  # 2
    print(fizz_buzz(79))  # 3
```
This script defines a helper function `count_digit_7` to count the occurrences of the digit 7 in a number. The main function `fizz_buzz` iterates over the numbers less than the input `n`, checks if they are divisible by 11 or 13, and increments the count by the number of 7s in each such number. The script then includes test cases to verify the correctness of the `fizz_buzz` function.