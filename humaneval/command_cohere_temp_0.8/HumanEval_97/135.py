```python
def multiply(a, b):
    """Returns the product of the unit digits of the provided integers."""
    return int(str(a)[-1]) * int(str(b)[-1])
```
The function leverages str[-1] to extract the unit digit of each number, these unit digits are then multiplied together to yield the final result. 

Here is a test drive code to verify the correctness of the given solution:
```python
def test_multiply():
    # Example 1
    assert multiply(148, 412) == 16, "Example 1 failed."

    # Example 2
    assert multiply(19, 28) == 72, "Example 2 failed."

    # Example 3
    assert multiply(2020, 1851) == 0, "Example 3 failed."

    # Example 4
    assert multiply(14, -15) == 20, "Example 4 failed."

    # Example 5
    assert multiply(123, 456) == 4, "Example 5 failed."

    print("All tests passed!")

test_multiply()
```

With the test code provided above, you can run the `test_multiply` function to validate the correctness of the `multiply` function.