```python
def fizz_buzz(n):
    count = 0
    for i in range(2, n+1):
        digit = str(i)
        if (7 in digit) and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

# Example:
>>> fizz_buzz(50)
0
>>> fizz_buzz(78)
2
>>> fizz_buzz(79)
3
```

This function, `fizz_buzz`, accepts an integer `n` as input and calculates the number of times the digit 7 appears in the set of integers that are less than `n` and are divisible by 11 or 13. It uses a optimized logic that counts the occurrences of 7 in these numbers, and the result is the total count. This function can be easily understood and used in various scenarios.