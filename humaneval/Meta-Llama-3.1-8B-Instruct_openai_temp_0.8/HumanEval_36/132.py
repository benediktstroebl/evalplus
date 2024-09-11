### Fizz Buzz Problem Solver
```python
def count_digit_7(n: int) -> int:
    """
    Count the occurrences of the digit 7 in the given number.
    
    Args:
    n (int): The input number.
    
    Returns:
    int: The number of occurrences of the digit 7.
    """
    count = 0
    for digit in str(n):
        if digit == '7':
            count += 1
    return count

def fizz_buzz(n: int) -> int:
    """
    Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive).
    
    Returns:
    int: The number of occurrences of the digit 7.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += count_digit_7(i)
    return count

# Example usage:
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script first defines a helper function `count_digit_7` to count the occurrences of the digit 7 in a given number. The main function `fizz_buzz` then iterates over the numbers less than the given upper limit `n` and checks if each number is divisible by 11 or 13. If it is, it calls `count_digit_7` to count the occurrences of the digit 7 in that number and adds the result to the total count.