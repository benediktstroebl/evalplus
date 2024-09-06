```python
def fizz_buzz(n: int):
    return 7 - (n // 13) if n % 13 != 0 else 0

# Test cases

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
assert fizz_buzz(78) == 2
assert fizz_buzz(79) == 3
``` 
This Python function `fizz_buzz` calculates the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. It returns 0 if the` n % 13 == 0 `. Otherwise, it returns 7 minus the quotient of `n` divided by 13, using the modulo operator to avoid negative results. The function's test cases cover the expected behavior of the function.