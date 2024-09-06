```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive """
    return f"0 {n} {n+1} {n+2} {n+3} ... {n} "

#Test case 0: Function should return '0'
test_case = string_sequence(0)
assert test_case == '0'

#Test case 1: Function should return '     '
test_case = string_sequence(1)
assert test_case == '     '

#Test case 2: Function should return '01234'
test_case = string_sequence(5)
assert test_case == '01234'

#Test case 3: Function should handle negative input
test_case = string_sequence(-5)
assert test_case == '-Bundle'
```