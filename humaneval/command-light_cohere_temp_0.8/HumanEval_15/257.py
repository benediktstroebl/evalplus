```python
def string_sequence(n: int) -> str:
    """ Returns a string containing space-delimited numbers starting from 0 and ending at n inclusive"""
    
    return f"0 {n}{" + str(n+1) + "}"

def test_string_sequence(test_cases):
    for case in test_cases:
        assert str(string_sequence(case)) == f"0 {case}{" + str(case+1) + "}"
```