```python
def fizz_buzz(n: int) -> int:
    if n < 7:
        return 0
    count = 0
    while n % 11 == 0 or n % 13 == 0:
        n /= 11
    while n > 0:
        count += n // 10
        n -= n // 10
    return count

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3
```
This code defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in a given number less than or equal to 80, which is the target range for the function. The function uses a iterative approach to count the occurrences of 7 and then returns the total count. The `test_fizz_buzz` function contains test cases that verify the correctness of the `fizz_buzz` function with different input values.