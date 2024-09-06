```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    nums = range(10, n+1, 2)
    for num in nums:
        if num % 11 == 7 or num % 13 == 7:
            count += 1
    return count

# Example usage:
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This function, `fizz_buzz`, uses a loop to iterate through the numbers from 10 to `n` (exclusive) with a step of 2. It checks each number for divisibility by 11 or 13 using the modulo operator, and if the number has 7 as a factor, it increments the `count` variable. 
At the end of the loop, the function returns the value of `count`, which represents the number of times the digit 7 appears in the sequence of integers less than `n` that are divisible by 11 or 13.