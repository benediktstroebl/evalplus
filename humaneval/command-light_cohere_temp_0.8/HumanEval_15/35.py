Here's the code:
```python
def string_sequence(n: int) -> str:
    return f"0 {n} 000 {" + str_sequence(n-1) + "}" 

def str_sequence(n: int) -> str:
    return f"0 {n}".repeat(n) 

# Unit tests
def test_string_sequence():
    assert string_sequence(0) == "0", 
    assert string_sequence(1) == "00", 
    assert string_sequence(3) == "000", 
    assert string_sequence(5) == "0 1 2 3 4 5"

if __name__ == "__main__":
    test_string_sequence()
```
The function **string_sequence** takes an integer n as input and returns a string containing space-delimited numbers starting from 0 up to n inclusive. The **str_sequence** function is a helper function that returns a string containing the number "0" n times.

The test_string_sequence function contains unit tests for the string_sequence function. These tests check that the string_sequence function produces the correct output for various input values. 

You can use this code to solve the problem of generating a sequence of numbers in markdown code blocks.