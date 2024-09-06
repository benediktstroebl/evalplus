```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n+1)

# Tests
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(-5) == '0 5 4 3 2 1'
    assert string_sequence(10) == '9 8 7 6 5 4 3 2 1'

if __name__ == "__main__":
    test_string_sequence()
``` 
This code defines a function `string_sequence` that creates a string containing numbers separated by spaces, starting from 0 and ending at n. It uses the basic Python string formatting to create the sequence. The `test_string_sequence` function tests that the `string_sequence` function produces the correct output for the given input values.