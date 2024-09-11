```python
def count_sevens_divisible_by_either(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        # Check if i is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to string to easily check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count

# Test cases
def fizz_buzz(n: int) -> int:
    return count_sevens_divisible_by_either(n)

print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

Note that this script defines two functions: `count_sevens_divisible_by_either` which does most of the work, and `fizz_buzz` which is the same as the original `fizz_buzz` function but calls the more descriptive `count_sevens_divisible_by_either` function. This follows the principle of single responsibility and makes the code easier to understand and maintain.