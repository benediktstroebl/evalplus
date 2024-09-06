Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    numbers = [num for num in range(n + 1)]  # Generate a list of numbers from 0 to n inclusive
    filtered_numbers = [num for num in numbers if num % 11 == 0 or num % 13 == 0]
    
    # Count the occurrences of digit 7 in the filtered numbers
    seven_count = sum(1 for num in filtered_numbers if num % 10 == 7)
    
    return seven_count

# Test cases
print(fizz_buzz(50))  # Should print 0
print(fizz_buzz(78))  # Should print 2
print(fizz_buzz(79))  # Should print 3
```

This code generates a list of numbers from 0 to `n` inclusive, filters this list to include only those numbers divisible by 11 or 13, and then counts the number of times the digit 7 appears in the filtered numbers to provide the answer.