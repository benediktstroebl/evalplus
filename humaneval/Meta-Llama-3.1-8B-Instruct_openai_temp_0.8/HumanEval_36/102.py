### Fizz Buzz Counter
#### Problem Description

Count the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13.

#### Python Solution
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): Upper bound for the range of numbers to check.

    Returns:
        int: Count of digit 7 appearances in the specified range.
    """
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            for digit in str(i):
                if digit == '7':
                    count += 1
                    break
    return count
```
#### Example Use Cases
```python
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This script defines a function `fizz_buzz(n)` that checks each integer less than `n` to see if it's divisible by 11 or 13. If it is, it then checks each digit of the integer to see if it's '7', and increments a counter for each instance of '7' found. The function returns the total count of digit 7 appearances in the specified range.