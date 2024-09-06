```python
def sum_to_n(n):
    """Returns the sum of the first n integers.

    Args:
        n (int): The highest number to be included in the sum.

    Returns:
        int: The sum of integers from 1 to n (inclusive).
    """
    return n * (n + 1) // 2  # Sum formula for integers from 1 to n

# Test cases
assert sum_to_n(30) == 465
assert sum_to_n(100) == 5050
assert sum_to_n(5) == 15
assert sum_to_n(10) == 55
assert sum_to_n(1) == 1
```

The function employs the sum formula for the first n positive integers: `n(n+1)/2`. This formula has been effectively implemented to calculate the sum of numbers from 1 to `n` and is encapsulated within the `sum_to_n` function.

The test cases, integrated within the script, verify the function's behavior through a variety of inputs. Each case employs the `assert` statement to ensure that the function's output agrees with the anticipated result.

To test it independently, navigate to the script in the terminal and input `python sum_to_n-test.py`. Upon executing this command, the test runner will assess the function's behavior against the existing test cases and deliver an overview of the outcomes. If all assertions hold true, this indicates the function's correct operation.