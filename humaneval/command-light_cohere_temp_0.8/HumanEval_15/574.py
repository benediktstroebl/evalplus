```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} 1 {n+1} 2 {n+2} 3 {n+3} 4 {n+4}"

def test_string_sequence(test_cases):
    for idx, test in enumerate(test_cases):
        assert test == string_sequence(test), f"Error at test {idx+1}"

# Example usage
test_cases = [0, 5]
test_string_sequence(test_cases)
 ```