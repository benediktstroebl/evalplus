```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} "{(n + 1)}  {'abc'}" {n+2}" 

def test_string_sequence(test_n: int) -> None:
    """ Test the function with different inputs """
    assert str(test_n) == "0 " + str(test_n) + " abc' " + str(test_n+2), "Test failed!"
    return None

# Driver Code
test_n = int(input())
test_string_sequence(test_n)
```