```python
def change_base(x: int, base: int):
    if isinstance(x, str):
        x = int(x[::-1])  # Convert string to integer
    return f"{x:0>{base}"}  # Format the number with base

def test():
    base = 10
    x = "8"
    assert change_base(x, base) == "22"
    base = 2
    x = "1000"
    assert change_base(x, base) == "2200"
    base = 7
    x = "111"
    assert change_base(x, base) == "1111"

# Run the tests
test()
```
This script defines a function `change_base` that converts a given number `x` to a different base `base`. It handles the case of input being a string by converting it to an integer using `int(x[::-1])`. The `test` function contains tests that verify the correctness of the `change_base` function with various input combinations. The test function uses the expected output to pass the tests.