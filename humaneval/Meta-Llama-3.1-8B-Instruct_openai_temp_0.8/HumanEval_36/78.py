```markdown
### Fizz Buzz Problem Solver

#### Problem Description
Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

#### Solution

```python
def fizz_buzz(n: int):
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit for the range of numbers to check.
    
    Returns:
        int: The number of times the digit 7 appears in the specified range.
    """
    count = 0  # Initialize a counter for the digit 7
    for i in range(n):  # Iterate over the range of numbers
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string for digit checking
            count += str_i.count('7')  # Count the occurrences of the digit 7
    return count  # Return the final count

### Example Usage

print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script defines a function `fizz_buzz` that takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function uses a loop to iterate over the range of numbers, checks for divisibility by 11 or 13, and counts the occurrences of the digit 7 in the strings representation of the numbers. The example usage demonstrates the function's behavior with different inputs.