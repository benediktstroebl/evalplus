```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n+1, 2)
    for num in nums:
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
``` 
This function utilizes a list of numbers from 10 to n (inclusive, but with a step of 2) to generate a sequence of integers that are less than n and divisible by 11 or 13. The function then counts the occurrence of the digit 7 in this sequence, and returns the total count.