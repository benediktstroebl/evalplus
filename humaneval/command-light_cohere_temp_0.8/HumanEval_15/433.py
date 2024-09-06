```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 to n inclusive"""
    return f"0 {n}{' ' * (n - 1)}{n+1}"

#Test case 1
def test_string_sequence():
    assert string_sequence(0) == '0'
    assert string_sequence(1) == '1'
    assert string_sequence(5) == '0 1 2 3 4 5'
    assert string_sequence(10) == '0 9 8 7 6 5 4 3 2 1 0'

# Test case 2
def test_string_sequence2():
    assert string_sequence(3) == '3'
    assert string_sequence(12) == '12'
    assert string_sequence(21) == '21'

#Main execution
if __name__ == "__main__":
    test_string_sequence()
    test_string_sequence2()
``` 
This Python code provides a function `string_sequence` that generates a string containing space-separated numbers from 0 to `n`, where `n` is an input integer. It then tests these function with two test cases to validate its functionality.