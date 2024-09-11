### Fizz Buzz Counter
#### Python Script

```markdown
### Fizz Buzz Counter
#### Problem Description
Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

#### Code
```python
def count_sevens(n: int) -> int:
    """
    Count the occurrence of digit 7 in numbers less than n that are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit.
    
    Returns:
        int: The number of times the digit 7 appears.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily check for the presence of '7'
            str_i = str(i)
            count += str_i.count('7')
    return count


def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
        n (int): The upper limit.
    
    Returns:
        int: The number of times the digit 7 appears.
    """
    return count_sevens(n)


### Example Usage
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

#### Explanation
This script defines two functions: `count_sevens` and `fizz_buzz`. The `count_sevens` function counts the occurrence of the digit 7 in numbers less than a given limit `n` that are divisible by 11 or 13. The `fizz_buzz` function simply calls `count_sevens`. The script then demonstrates the usage of these functions with example inputs.