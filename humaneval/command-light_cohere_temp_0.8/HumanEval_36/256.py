Here is a self-contained Python script with a function that solves the problem of counting the occurrences of the number 7 in numbers less than n, which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    def count_7s(number: int):
        return any(number % 11 == 7) or any(number % 13 == 7)

    return count_7s(n)

# Test cases
print(fizz_buzz(50))  # Output: 0
print(fizz_buzz(78))  # Output: 2
print(fizz_buzz(79))  # Output: 3
```

This script provides a self-contained solution for the given problem.  It also contains a function called count_7s, which uses the any function to check for the existence of 7 in the number less than n, when dividing by 11 or 13.