```python
def count_seven_appearances(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n - 1, -1, -1):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count


def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_seven_appearances(n)


# Test the function
if __name__ == "__main__":
    print(fizz_buzz(50))  # Output: 0
    print(fizz_buzz(78))  # Output: 2
    print(fizz_buzz(79))  # Output: 3
```

Note that the original function name `fizz_buzz` might be misleading because it doesn't actually implement the traditional FizzBuzz algorithm. Instead, I've named the function `count_seven_appearances` to better reflect its purpose, and used the `fizz_buzz` name only for backwards compatibility with the original docstring.