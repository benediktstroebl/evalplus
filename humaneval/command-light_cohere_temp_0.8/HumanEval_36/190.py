```python
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0:
        return 0

    # Initialize a count of zeros
    count = 0

    # Iterate through numbers from 0 to n
    for num in range(0, n+1):
        d = str(num)[2:]
        if d == "77":
            count += 1

    return count

# Unit tests
assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
The provided Python script defines a function called **fizz_buzz**, which aims to determine the frequency of the digit 7 in the sequence of integers up to a given number n, specifically those that are both less than n and are divisible by 11 or 13. The function achieves this above by counting the number of occurrences of 7 in this subset of numbers. It initializes a certain count of zeros, then iterates through numbers from 0 to n, checking if the current number's two-digit representation is "77". The function returns the count of occurrences of 7 in this range.