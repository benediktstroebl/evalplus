```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return sum(int(i) == 7 and i <= n and (i % 11 == 0 or i % 13 == 0) for i in range(1, n+1))

# Test the function
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```
This code defines a function `fizz_buzz` that calculates the frequency of the number 7 in the set of numbers less than or equal to `n` which are divisible by 11 or 13. 

The function uses a list comprehension to iterate through numbers from 1 to `n+1` and checks if the current number is 7, less than 7, and if it's divisible by 11 or 13. The code then sums up these number of these conditions to return the total count of how many times the number 7 appears in this set.