```python
def string_sequence(n: int) -> str:
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    if n <= 0:
        return ""
    return f" {n} " * str_sequence(n - 1)

def test_string_sequence():
    assert str_sequence(0) == "0", "Test passed"
    assert str_sequence(1) == "1", "Test passed"
    assert str_sequence(5) == "0 1 2 3 4 5", "Test passed"
    assert str_sequence(10) == "0 9 8 7 6 5 4 3 2 1" , "Test failed"

if __name__ == "__main__":
    test_string_sequence()
```
The test function runs the `str_sequence` function with various input values and verifies the output against the expected results. 
If all tests pass, the code is considered valid.