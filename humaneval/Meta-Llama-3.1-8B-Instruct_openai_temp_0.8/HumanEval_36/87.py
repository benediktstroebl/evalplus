```markdown
### Fizz Buzz Problem Solver

This script solves the Fizz Buzz problem, counting the occurrences of the digit 7 in integers less than n that are divisible by 11 or 13.

#### Code
```python
def fizz_buzz(n: int) -> int:
    """
    Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

    Args:
        n (int): The upper limit.

    Returns:
        int: The count of digit 7 occurrences.
    """
    count = 0  # Initialize count to 0
    for i in range(1, n):  # Loop through all integers less than n
        if i % 11 == 0 or i % 13 == 0:  # Check if the number is divisible by 11 or 13
            str_i = str(i)  # Convert the number to a string
            count += str_i.count('7')  # Count the occurrences of '7'
    return count

# Test cases
print(fizz_buzz(50))  # Expected output: 0
print(fizz_buzz(78))  # Expected output: 2
print(fizz_buzz(79))  # Expected output: 3
```

#### Explanation

1. We initialize a `count` variable to keep track of the occurrences of the digit 7.
2. We loop through all integers less than `n`.
3. Inside the loop, we check if the current number is divisible by 11 or 13. If it is, we convert it to a string and count the occurrences of '7'.
4. We add the count of '7' to the total `count`.
5. Finally, we return the total count.

This script uses a simple and efficient approach to solve the Fizz Buzz problem.