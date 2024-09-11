```markdown
### Fizz Buzz 7 Counter
#### Problem Description
Count the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.

#### Solution

```python
def count_digit_7(n: int) -> int:
    """Count the number of times the digit 7 appears in numbers less than n which are divisible by 11 or 13."""
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    return count_digit_7(n)

# Test cases
print(fizz_buzz(50))   # 0
print(fizz_buzz(78))   # 2
print(fizz_buzz(79))   # 3
```

### Explanation
The `fizz_buzz` function takes an integer `n` as input and returns the count of the digit 7 in numbers less than `n` that are divisible by 11 or 13. It uses a helper function `count_digit_7` to achieve this. The `count_digit_7` function iterates over all numbers less than `n`, checks if each number is divisible by 11 or 13, and counts the occurrences of the digit 7 in each such number. The results are summed up and returned.

This solution uses a simple and efficient approach to solve the problem, with a time complexity of O(n).