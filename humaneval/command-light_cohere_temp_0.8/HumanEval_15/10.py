Here is a self-contained Python script that defines a function `string_sequence` that generates a string containing space-delimited numbers starting from 0 up to the number `n` passed as an argument:
```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str_sequence(n - 1) + "}"

def str_sequence(n: int) -> str:
    return "".join(str(i) for i in range(n))

#unit tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(5) == '0 1 2 3 4 5'
```
The above code provides a function that generates a string with numbers up to the passed in number, and a test function to check the output of this function.