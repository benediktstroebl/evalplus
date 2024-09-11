```markdown
### Fizz Buzz Counter
#### Problem Description
Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

#### Code
```python
def fizz_buzz(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper bound.

    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the digit 7
            str_i = str(i)
            # Count the occurrences of the digit 7
            count += str_i.count('7')
    return count
```

#### Example Usage
```python
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

#### Note
This script iterates over all integers less than `n` and checks if they are divisible by 11 or 13. If they are, it counts the occurrences of the digit 7 in the string representation of the number. The total count is then returned. This approach has a time complexity of O(n), where n is the input value.
```