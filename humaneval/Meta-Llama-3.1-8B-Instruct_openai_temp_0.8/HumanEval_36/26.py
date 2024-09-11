```markdown
### Fizz Buzz Problem Solution

#### Problem Statement

Return the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Solution

```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit (exclusive).

    Returns:
        int: The count of digit 7 appearances.
    """
    count = 0
    for i in range(n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check each digit
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

This script defines a function `fizz_buzz(n)` that iterates over all integers less than `n`, checks if each number is divisible by 11 or 13, and counts the occurrences of the digit 7 in those numbers. The function returns the total count of digit 7 appearances. The example usage demonstrates the function's behavior with the provided test cases.