```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive. 
    >>> string_sequence(0) 
    --> ['0'] 
    >>> string_sequence(1) 
    --> ['0', '1'] 
    >>> string_sequence(5) 
    --> ['0', '1', '2', '3', '4', '5'] 
    """
    return ["".join([str(i) for i in range(n)])

def test_string_sequence():
    """
    Test the function with different values for n and ensure the output is as expected.
    """
    assert string_sequence(0) == ['0'], "Failed with n=0"
    assert string_sequence(1) == ['0', '1'], "Failed with n=1"
    assert string_sequence(5) == ['0', '1', '2', '3', '4', '5'], "Failed with n=5"

if __name__ == "__main__":
    test_string_sequence()
 ```
We've provided a self-contained Python script that defines a function `string_sequence` that generates a string of space-separated numbers from 0 to n, and tests this function with various input values.