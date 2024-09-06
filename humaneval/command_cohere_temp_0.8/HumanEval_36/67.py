Here's a Python script that contains a function fizz_buzz(n) which solves the problem as per the test cases provided:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a generator expression using yield to produce integers from 1 up to n in increments of 1.
    yield from (i for i in range(1, n+1))    # Yield each integer once before filtering.
    
    # Use two separate filtering conditions using & and | to calculate divisibility by 11 or 13.
    for i in range(1, n):
        if (i % 11) == 0 or (i % 13) == 0:
            # Count the number of 7s in the integer value of i.
            yield (i if i != 7 else 0) + (7 if i == 7 else 0) in range(1, n)

# Test cases
import pytest

@pytest.mark.parametrize('test_input, expected', [
    (50, 0),
    (78, 2),
    (79, 3)
])
def test_fizz_buzz(test_input, expected):
    """Test the fizz_buzz function for various input values."""
    result = fizz_buzz(test_input)
    assert result == expected, "fizz_buzz({}) did not return {} as expected.".format(test_input, expected)
```

This script defines the fizz_buzz function, which uses a generator expression to generate integers from 1 to n and then filters those that are divisible by either 11 or 13. For each qualifying number, it counts the number of 7s and yields the result. The script also includes test cases that show how the function can be tested to verify if it produces the expected results for different inputs. You can add these test cases to your Python file to ensure the correctness of your function. 
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    for i in range(1, n+1):
        if (i % 11) == 0 or (i % 13) == 0:
            yield (i if i != 7 else 0) + (7 if i == 7 else 0) in range(1, n+1)

# Test cases
for i in [50, 78, 79]:
    print(fizz_buzz(i), end='')
```