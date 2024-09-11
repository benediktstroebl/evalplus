### Fizz Buzz with Digit 7 Counter
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound.

    Returns:
        int: The number of times 7 appears.
    """
    count = 0
    for num in range(n):
        # Check if the number is divisible by 11 or 13
        if num % 11 == 0 or num % 13 == 0:
            # Convert the number to a string for digit counting
            num_str = str(num)
            # Count the occurrences of '7' in the string
            count += num_str.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```
This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function iterates over the range from 0 to `n-1`, checking each number for divisibility by 11 or 13, and counting the occurrences of '7' in the string representation of each number. The result is then returned. The script also includes test cases to verify the correctness of the function.