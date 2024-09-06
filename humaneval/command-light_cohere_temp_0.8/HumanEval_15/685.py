Here's the self-contained Python script that implements the string sequence function from the prompt:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4} 5"

def test_string_sequence():
    assert string_sequence(0) == '0', "Should start with 0"
    assert string_sequence(1) == '1', "Should add 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Should reach 5"
    assert string_sequence(6) == '6', "Should start a new sequence"

# Call the test function and print the results
print(test_string_sequence())
```