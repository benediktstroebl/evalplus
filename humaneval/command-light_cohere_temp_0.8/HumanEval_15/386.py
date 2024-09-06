```python
def string_sequence(n: int) -> str:
    return f"0 {n}" * (n + 1)

def test_string_sequence():
    assert str(string_sequence(0)) == '0', "Test case 0 failed"
    assert str(string_sequence(1)) == '1', "Test case 1 failed"
    assert str(string_sequence(5)) == '0 1 2 3 4 5', "Test case 5 failed"

if __name__ == "__main__":
    test_string_sequence()
``` 
This script defines a function `string_sequence` which creates a string that contains numbers separated by spaces, starting from 0 up to the given number `n` (inclusive). The `test_string_sequence` function contains assertions to check if the function behaves correctly for various input values.  The test_string_sequence is then called to verify if the function produces the correct output for the test cases.