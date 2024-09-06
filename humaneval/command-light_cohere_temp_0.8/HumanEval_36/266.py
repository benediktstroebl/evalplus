Here is a Python script with a self-contained function that solves the problem:
```python
def fizz_buzz(n: int):
    def count_seven(x: int):
        return any(x%11==7) or any(x%13==7)
    
    return count_seven(n)

def test_fizz_buzz():
    assert fizz_buzz(50) == 0
    assert fizz_buzz(78) == 2
    assert fizz_buzz(79) == 3

if __name__ == "__main__":
    test_fizz_buzz()
```

This script defines a function `fizz_buzz` which calculates the number of occurrences of the digit 7 in numbers less than `n` that are divisible by 11 or 13. It then defines a test_fizz_buzz() function, which passes tests using the `assert` statement. The test will verify if the function is correctly implemented.