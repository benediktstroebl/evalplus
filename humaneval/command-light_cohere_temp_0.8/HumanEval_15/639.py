```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n}..."join(str(x) for x in range(n+1))

if __name__ == "__main__":
    assert string_sequence(0) == "0", "0 should be equal to '0'"
    assert string_sequence(1) == "1", "1 should be equal to '1'"
    assert string_sequence(5) == "0 1 2 3 4 5", "For n = 5, the sequence should be: 0 1 2 3 4 5"
    assert string_sequence(10) == "0 9 8 7 6 5 4 3 2 1", "For n = 10, the sequence should be: 0 9 8 7 6 5 4 3 2 1"
    assert string_sequence(15) == "0 14 13 12 11 10 8 7 5 3 2 1", "For n = 15, the sequence should be: 0 14 13 12 11 10 8 7 6 5 3 2"
    assert string_sequence(2) == "0 2", "For n = 2, the sequence should be: 0 2"
```
This Python code defines a function called string_sequence that takes an integer n as input and returns a string containing space-separated numbers from 0 to n, with each number separated by a single space. The code then verifies the test the validity of this function by asserting that the output of the string_sequence function is correct for a range of values from 0 to 15. 

This is just one possible, if you'd like to see other test cases, you can easily add the test conditions within the `assert` statement.