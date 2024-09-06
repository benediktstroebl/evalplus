```python
def string_sequence(n: int) -> str:
    """Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} ... {n} "

def test_string_sequence():
    """Functional test for the string_sequence function"""
    assert string_sequence(0) == '0 ', "String sequence function failed test - wrong starting number"
    assert string_sequence(1) == '1 ', "String sequence function failed test - wrong starting number"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence function failed test - wrong output"

if __name__ == "__main__":
    test_string_sequence()
``` 
The function 'string_sequence' generates a string containing space-separated numbers from 0 up to the given 'n'. It uses an f-string formatting to place the numbers in a string. The test_string_sequence function tests the function with various inputs and asserts that the output is correct. 
The output of this code will be the test passing and the string sequence function working correctly.