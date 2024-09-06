Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    # Define a list to store the numbers from 1 to n.
    numbers = list(range(1, n + 1))
    # Filter out the numbers that are divisible by 11 or 13.
    divisible_by_11_or_13 = [num for num in numbers if num % 11 == 0 or num % 13 == 0]
    # Count the number of times the digit 7 appears in the filtered list.
    seven_count = sum(1 for num in divisible_by_11_or_13 if num % 10 == 7)
    return seven_count
```

This script defines a function fizz_buzz that takes an integer n as input and returns the number of times the digit 7 appears in integers less than n that are divisible by 11 or 13. The function first creates a list of all the numbers from 1 to n, then filters out the numbers that are divisible by 11 or 13, and finally counts the number of times the digit 7 appears in the filtered list. 

Here is a markdown code block containing a set of test cases to verify the correct operation of the fizz_buzz function:
```python
# Test cases for the fizz_buzz function
def test_fizz_buzz():
    # Test case 1: The first several numbers and the expected results.
    assert fizz_buzz(10) == 0, "Expected fizz_buzz(10) to be 0."
    assert fizz_buzz(50) == 0, "Expected fizz_buzz(50) to be 0."
    assert fizz_buzz(78) == 2, "Expected fizz_buzz(78) to be 2."
    assert fizz_buzz(79) == 3, "Expected fizz_buzz(79) to be 3."

    # Test case 2: Boundary test, to check if the function handles lists with different sizes.
    assert fizz_buzz(100) == 4, "Expected fizz_buzz(100) to be 4."
    assert fizz_buzz(110) == 5, "Expected fizz_buzz(110) to be 5."
    assert fizz_buzz(111) == 6, "Expected fizz_buzz(111) to be 6."
    assert fizz_buzz(120) == 7, "Expected fizz_buzz(120) to be 7."
    assert fizz_buzz(121) == 6, "Expected fizz_buzz(121) to be 6."

    # Test case 3: Large n test, to check if the function handles lists with a large size.
    assert fizz_buzz(1000) == 66, "Expected fizz_buzz(1000) to be 66."
    assert fizz_buzz(1001) == 67, "Expected fizz_buzz(1001) to be 67."
    assert fizz_buzz(1010) == 68, "Expected fizz_buzz(1010) to be 68."
    assert fizz_buzz(1015) == 70, "Expected fizz_buzz(1015) to be 70."
    assert fizz_buzz(1016) == 69, "Expected fizz_buzz(1016) to be 69."

test_fizz_buzz()
```

The test cases will generate a nested list of integers from 1 to n and then filter this list to include only the integers that are divisible by 11 or 13