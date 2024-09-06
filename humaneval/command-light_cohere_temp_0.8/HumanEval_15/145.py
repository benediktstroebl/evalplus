```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n}{' ' * (n-1)}" 

def test_string_sequence(test_n: int) -> None:
    assert(str(test_string_sequence(test_n)) == f"0 {test_n}{' ' * (test_n-1)}", 
        "Test failed: incorrect output for n = {test_n}")
    return_

# Example usage
test_n = int(input("Enter a number to test: "))
test_string_sequence(test_n)
```