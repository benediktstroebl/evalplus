Here is a self-contained Python script that defines a function `string_sequence`:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {" + str(n+1) + "}" * (n+1)

def test_string_sequence():
    assert string_sequence(0) == "0",
    assert string_sequence(1) == "1",
    assert string_sequence(5) == "0 1 2 3 4 5"

# main code execution point
test_string_sequence()
```
The `string_sequence` function takes an integer `n` as input and returns a string containing space-delimited numbers starting from 0 up to `n` inclusive. The test_string_sequence function contains unit tests that verify the correctness of the `string_sequence` function for different input values.