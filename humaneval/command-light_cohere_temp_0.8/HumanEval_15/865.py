```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {" + string_sequence(n - 1) + "}" 

def test_string_sequence():
    """ Test case function """
    assert string_sequence(0) == '0', "Function does not return '0' for n = 0"
    assert string_sequence(1) == '1', "Function does not return '1' for n = 1"
    assert string_sequence(5) == '0 1 2 3 4 5', "Function does not return correct sequence for n = 5"
    assert string_sequence(10) == '0 10 11 12 13 14', "Function does not return correct sequence for n = 10"

# Main function to call test case and function
if __name__ == "__main__":
    test_string_sequence()
``` 
The function `string_sequence` takes an integer `n` as input and returns a string containing space-separated numbers from 0 to `n - 1` (inclusive). 
The function is designed to be self-contained, meaning it does not rely on any other functions or modules within the Python script. The test_string_sequence function is used to verify the correctness of the `string_sequence` function by providing test cases that should pass. The `main` function is the entry point of the script, and it calls the `test_string_sequence` function to run all the test cases.