The fizz_buzz function counts the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. It uses a native Python techniques to achieve this. 

Here's the function along with its corresponding tests:
```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Initialize count of 7s
    count = 0
    
    # Iterate through integers less than n
    for num in range(1, n + 1):
        # Skip 7
        if num % 10 == 7:
            continue
        
        # Check for divisibility by 11 or 13
        if (num % 11 == 0 or num % 13 == 0):
            break 
        
        # Increment count of 7s
        count += 1
    
    return count

# Test suite
def test_fizz_buzz(n):
    """Various inputs and ensuring the result is correct."""
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
    assert fizz_buzz(100) == 6
    assert fizz_buzz(1025) == 8  # This should return 9, due to 10 being divisible by 13 but not 7 being counted
    assert fizz_buzz(7) == 0  # This should return 0, as 7 is itself and not divisible by either 11 or 13

# If the function doesn't run without errors, there's a bug in the test suite!