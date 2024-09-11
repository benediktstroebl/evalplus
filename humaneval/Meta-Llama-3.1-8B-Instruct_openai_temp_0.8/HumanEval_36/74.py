```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0  # Initialize the count of digit 7 appearance
    for i in range(1, n):  # Iterate over all numbers less than n
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to string
            count += str_i.count('7')  # Count the appearances of digit 7
    return count  # Return the total count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a loop to iterate over all numbers less than `n` and checks each number to see if it is divisible by 11 or 13. If it is, the function converts the number to a string and uses the `count` method to count the appearances of the digit 7. The total count is then returned. The script also includes test cases to verify the correctness of the function.