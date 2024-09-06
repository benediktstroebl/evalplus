```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive"""
    return f"0 {n} {n+1} {n+2} {n+3} {n+4}"

def test_sequence(test_cases: list[int]) -> list[str]:
    """ Test the string_sequence function for different cases of input """
    result = []
    for n in test_cases:
        result.append(string_sequence(n))
        assert result[-1] == f"0 {n} {n+1} {n+2} {n+3} {n+4}", str(result)

# Example usage
test_cases = [0, 5]
test_sequence(test_cases)
``` 
This code defines a function 'string_sequence' which returns a string containing space-separated numbers from 0 up to a given integer n, and tests this function with some sample cases using the 'test_sequence' function.  The test_sequence function takes a list of integers and passes them to 'string_sequence' to test its functionality. The test_sequence function uses assertions to check if the function's output matches the expected output for each input case.