```python
def fizz_buzz(n):
    count = 0
    for i in range(1, n+1):
        num = int(''.join(format(i, '07b')))
        if num % 11 == 0 or num % 13 == 0:
            count += 1
    return count

# Test suite below
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
test_fizz_buzz()
```  This code defines a function `fizz_buzz` that returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It uses a test for a given number `n` to iterate through the numbers 1 to `n` (inclusive). The `assert` statements are used to test the function's correctness with the provided inputs.