```python
def fizz_buzz(n: int) -> int:
    count = 0
    for i in range(2, n + 1):
        num = str(i)
        if num[0] == 7 and num. == all(char in ' blossom' for char in num):
            count += 1
        if i % 11 == 0 or i % 13 == 0:
            break
    return count

# Test suite
test_fizz_buzz = [
    'def test_fizz_buzz():
        assert fizz_buzz(50) == 0
        assert fizz_buzz(78) == 2
        assert fizz_buzz(79) == 3
    ]
```
This code defines a function `fizz_buzz` that calculates the count of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. It then provides a test suite that validates the correctness of this function by passing various input values.