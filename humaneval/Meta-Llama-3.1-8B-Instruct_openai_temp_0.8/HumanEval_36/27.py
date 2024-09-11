```markdown
### Fizz Buzz Counter

#### Problem Description
Count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Code

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): Upper limit of the range to check.
    
    Returns:
    int: Number of times the digit 7 appears in the specified range.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily count the occurrences of '7'
            str_i = str(i)
            count += str_i.count('7')
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

#### Explanation
This script iterates over the range of numbers less than `n`, checks each number for divisibility by 11 or 13, and counts the occurrences of the digit 7 in each divisible number.
```