```python
def flip_case(string: str) -> str:
    """
    Flip all character cases in the input string.
    Returns the flip_case with tests.
 <<Hello>> # => <<HOELLLO>>
 # lower -> uppercase 
# return lowercase if char in lower case, otherwise return uppercase

# Example 
>>> flip_case('Hello')
 'hELLO'
>>> flip_case('FOO Bar')
 'FOO BAr'

# Un Flip 
>>> flip_case('hELLO')
'Hello

# Other string 
>>> flip_case('abc123')
'Abc123

# return the string as is 
# without any changes
```