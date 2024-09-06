```python
def fizz_buzz(n: int):
    count = 0
    for num in range(1, n+1):
        if is_divisible_by_11_13(num):
            count += 7
    return count

def is_divisible_by_11_13(num:
    return num % 11 == 0 or num % 13 == 0)

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

# Main driver to run the functions
if __name__ == "__main__":
    test_fizz_buzz()
```
This script defines a function `fizz_buzz` that calculates the number of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. The function uses a `is_divisible_by_11_13` helper function to check divisibility. The `test_fizz_buzz` function contains unit tests that validate the behavior of the `fizz_buzz` function for different input values. The `__main__` block allows the script to be executed as a standalone program.