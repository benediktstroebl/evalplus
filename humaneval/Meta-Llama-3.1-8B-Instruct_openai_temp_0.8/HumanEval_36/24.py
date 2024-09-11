### Fizz Buzz Problem Solver
#### Python Script
```markdown
def count_digit_seven(n: int) -> int:
    """Count the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive).
    
    Returns:
    int: The count of digit 7 in the specified numbers.
    """
    count = 0
    for i in range(1, n):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # Convert the number to a string to easily count the digit 7
            str_i = str(i)
            count += str_i.count('7')
    return count


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    
    Args:
    n (int): The upper limit (exclusive).
    
    Returns:
    int: The count of digit 7 in the specified numbers.
    """
    return count_digit_seven(n)


# Test cases
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```
This script defines two functions: `count_digit_seven` and `fizz_buzz`. The `count_digit_seven` function counts the occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The `fizz_buzz` function is a wrapper around `count_digit_seven` and provides the same functionality.

The test cases at the end verify the correctness of the implementation.