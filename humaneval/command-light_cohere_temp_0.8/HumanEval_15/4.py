```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n}..."

def test_string_sequence():
    """ Test the function with parameters 0 and 5, expecting the output to be '0 0 1 2 3 4 5'"
    assert string_sequence(0) == '0', "Function did not return 0"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function did not return expected output"

# Call the function with parameter 0 and display the output
print(string_sequence(0)) 

# Call the function with parameter 5 and display the output
print(string_sequence(5)) 

test_string_sequence()
```