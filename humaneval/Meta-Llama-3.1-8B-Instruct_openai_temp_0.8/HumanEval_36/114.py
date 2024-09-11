```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound for the numbers to check.

    Returns:
        int: The number of times the digit 7 appears in the specified range of numbers.
    """
    count = 0  # Initialize a counter to store the occurrences of 7
    for num in range(1, n):  # Iterate over numbers less than n
        if num % 11 == 0 or num % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_num = str(num)  # Convert the number to a string to easily check for '7'
            count += str_num.count('7')  # Increment the counter by the number of times '7' appears in the string
    return count  # Return the total count of '7' occurrences


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz(n)` that iterates over numbers less than `n`, checks if they are divisible by 11 or 13, converts the numbers to strings to easily check for the digit '7', and increments a counter by the number of times '7' appears in each string. The function returns the total count of '7' occurrences. Finally, the script includes test cases to verify the function's correctness.