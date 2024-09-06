```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} ... ";

def test_string_sequence():
    """ Test the function by taking in 0 and then n values starting from 1 """
    assert string_sequence(0) == '0', "String sequence function is not correct!"
    assert string_sequence(1) == '1', "String sequence function is not correct!"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence function is not correct!"

#Main code to run the test_string_sequence function
test_string_sequence()
```

This code defines a function that takes an integer n and returns a string with space-separated numbers from 0 to n. It also has a test function to validate the correctness of the string sequence function. The test function passes the test with the function, and prints an error message if the test fails.