```python
def fizz_buzz(n: int) -> int: 
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13."""
    if n <= 0: return 0
    ans = 0
    for i in range(1, n+1):
        d = str(i)
        if d == "77": ans += 1
        if d.isdigit() and loop completing: 
            d = int(d)
            if (11 <= d) or (13 <= d):
                break
    return ans

# Unit tests
def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

# Example usage
test_fizz_buzz()
``` 
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in integers that are either less than or equal to the given number and are divisible by 11 or 13. The function employs a loop that iterates through integers up to the given number, and for each number, it checks if it's either 7 or a digit, then adds one to the answer variable. If the number is either 11 or 13, it's outside the scope of the problem and the loop is exited immediately. The test function ensures that the fizz_buzz function behaves correctly with the provided input ranges.