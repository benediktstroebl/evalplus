Here's a Python script with a self-contained function `fizz_buzz` that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Filter out numbers less than n, include only those divisible by 11 or 13
    relevant_numbers = [num for num in range(n) if num % 11 == 0 or num % 13 == 0]
    
    # Count the occurrences of digit 7 in the filtered numbers
    sevens_occurrences = sum(1 for num in relevant_numbers if num % 10 == 7)
    
    return sevens_occurrences

# Test cases
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```

This script defines the `fizz_buzz` function, explains its logic, and provides test cases to ensure it behaves as expected. Please let me know if you would like me to explain any part of the code in further detail.