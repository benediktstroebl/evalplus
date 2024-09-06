Here is a self-contained Python script that solves the problem of counting the number of times the digit 7 appears in integers less than a given number n which are divisible by 11 or 13:
```python
def fizz_buzz(n: int):
    def count_seven_in_divisibles(num: int):
        return sum(map(lambda x: x == 7, num if num % 11 == 0 or num % 13 == 0))
    return count_seven_in_divisibles(n)

# Test suite
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

if __name__ == "__main__":
    test_fizz_buzz()
```

This script defines the function `fizz_buzz`, which takes an integer `n` as input and returns the number of times the digit 7 appears in integers less than `n` which are divisible by 11 or 13. The function `count_seven_in_divisibles` generates a list of all numbers less than `n` and checks if they are divisible by 11 or 13. If the number is divisible by either of these, it returns True, and otherwise, False. The function then sums up these results and returns the count of 7s.

Finally, the test suite is used to check the function's correctness. The `test_fizz_buzz` function will run this test automatically when the script is executed.