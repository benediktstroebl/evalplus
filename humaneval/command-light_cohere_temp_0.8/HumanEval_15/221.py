```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 upto n inclusive""" 
    return f"0 {n} {n+1} {n+2} {n+3}..."

def test_string_sequence(test_case: int) -> None:
    actual_result = string_sequence(test_case)
    expected_result = "".join print(f"Test case {test_case}: {actual_result} != {expected_result}")
    return None
```