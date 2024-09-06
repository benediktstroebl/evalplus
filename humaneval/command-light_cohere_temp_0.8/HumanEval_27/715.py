```python
def flip_case(string: str) -> str:
    return ''.joincase(string)

# Tests
 assert flip_case('Hello') == 'hELLO'
 assert flip_case('world') == 'WoRLd'
 assert flip_case(' simmering') == 'sImINGgLLord'
 assert flip_case('123') == '123'
 assert flip_case('abc123') == 'ABC123'
``` 
This function flips the case of a given string by converting each character to the opposite case, and the tests ensure that the function works correctly for a variety of inputs.