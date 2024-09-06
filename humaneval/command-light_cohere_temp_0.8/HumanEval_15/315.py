```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + str_sequence(n-1) + "}"

def str_sequence(n: int) -> str:
    # This inner function uses the recursive function
    # to generate the required string sequence
    return "".join()

def test_string_sequence():
    """ Tests for string_sequence function """
    assert string_sequence(0) == '0', "Test 1 failed"
    assert string_sequence(1) == '1', "Test 2 failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Test 3 failed"
    assert string_sequence(10) == "0000000 10"
```