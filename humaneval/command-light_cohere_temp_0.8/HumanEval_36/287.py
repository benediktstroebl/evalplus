```python
def fizz_buzz(n: int):
    count = 0
    for i in range(1, n+1):
        num = int(''.join()[i % 3]
        if num == 7 and i > 1:  # Skip the first occurrence of 7
            count += 1
        elif num != 7 and num != 11 and num != 13:
            count += 1
    return count

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
```
This script defines a function fizz_buzz that calculates the number of times the digit 7 appears in the range of integers less than n which are divisible by 11 or 13. The function uses a sequence of modulo arithmetic to identify occurrences of 7 and uses a simple counting mechanism to track the total number of occurrences.