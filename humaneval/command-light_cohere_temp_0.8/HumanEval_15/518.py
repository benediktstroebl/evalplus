```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {" + str(n+1) + "}" * (n+1)

def test_string_sequence(test_num: int) -> None:
    try:
        got = string_sequence(test_num)
        assert got == f"0 {test_num} {" + str(test_num+1) + "}", "AssertionError: Test failed"
    except AssertionError as ae:
        print(f"AssertionError: {ae}")
        assert False, "Error: Test should have passed"
    return None

# Test the function
test_string_sequence(10)
```