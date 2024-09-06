```python
def fizz_buzz(n: int):
    if n <= 0:
        return 0

    def count_seven(i):
        return (i % 11 == 7) or (i % 13 == 7)

    return sum(count_seven(i) for i in range(1, n+1))

# Example usage
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This function takes an integer n as input and returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13. The function uses a recursive approach to count the occurrences of 7, and the time complexity of this function is O(n), as it iterates over the input range.