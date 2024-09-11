```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Parameters:
    n (int): The upper limit of the range to check.
    
    Returns:
    int: The number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the presence of '7'
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # 0
print(fizz_buzz(78))  # 2
print(fizz_buzz(79))  # 3
```

This script defines a function called `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a simple loop to iterate over the range of integers less than `n`, checks each integer for divisibility by 11 or 13, converts the integer to a string to easily check for the presence of '7', and increments the count accordingly. The function is then tested with the provided test cases.