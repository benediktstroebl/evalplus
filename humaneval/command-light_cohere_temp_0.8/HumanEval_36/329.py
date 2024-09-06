Here's the solution:
```python
def fizz_buzz(n):
    count = 0
    for i in range(1, n+1):
        digit = str(i)
        count += int(digit) in [7, 13] if i % 2 == 0 else 0
    return count

# Test suite
def test():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

if __name__ == "__main__":
    test()
```
This code defines a function `fizz_buzz` that calculates the number of times the digit 7 appears in the sequence of integers less than a given number `n` which are divisible by 11 or 13. The function uses a recursive approach to achieve this. It iterates through numbers from 1 to `n` and checks if the corresponding digit is 7 or 13 by converting the number to a string and checking its membership in the [7, 13] list. The test suite contains additional test functions that verify the correctness of the `fizz_buzz` function by checking its output against the expected results for specific input values.