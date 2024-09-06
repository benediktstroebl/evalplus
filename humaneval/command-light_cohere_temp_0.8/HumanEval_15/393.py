```python
def string_sequence(n: int) -> str:
    """ 
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0) 
    '0'
    >>> string_sequence(5) 
    '0 1 2 3 4 5'
    """
    return f"0 {n}" * (n+1) 

def test_string_sequence(test_cases: list) -> None:
    for test in test_cases:
        assert string_sequence(test) == test 
        print("Test passed", end='')
```