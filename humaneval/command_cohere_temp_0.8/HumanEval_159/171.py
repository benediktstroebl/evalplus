Here's a Python script that contains a function eat() that solves the problem described in the code block above:
```python
def eat(n, need, rem):
    return [n + need, rem - need]

# Test cases
def test_eat():
    assert eat(5, 6, 10) == [11, 4]
    assert eat(4, 8, 9) == [12, 1]
    assert eat(1, 10, 10) == [11, 0]
    assert eat(2, 11, 5) == [7, 0]

test_eat()
```

This script defines the `eat()` function that takes three integers `n`, `need`, and `rem` as input and returns a list containing two integers as described in the prompt. It then includes a test module with functions prefixed with `test_` which can be executed by the `test_eat()` function to validate the correctness of the `eat()` function.