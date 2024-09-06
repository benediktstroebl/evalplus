Here is a Python script with a self-contained function that solves the problem of generating a sequence of numbers:
```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {1:.join(range(1, n+1))}"

def test_string_sequence():
    """Function to test the string_sequence function"""
    assert string_sequence(0) == '0', "String sequence fails for 0"
    assert string_sequence(1) == '1', "String sequence fails for 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "String sequence doesn't generate correct output for 5"

if __name__ == "__main__":
    test_string_sequence()
```
This code defines a function `string_sequence` which generates a sequence of numbers starting from 0 and ending at N, with each value separated by a space. 

The function is then tested using the `test_string_sequence` function, which checks if the `string_sequence` function generates the correct output for the given input.