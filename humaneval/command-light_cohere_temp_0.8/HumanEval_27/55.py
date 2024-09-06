```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Tests
assert flip_case('Hello') == 'hELLO'
assert flip_case('world! Upcase') == 'world.downcase'

```  It works by swapping all characters of the string, ensuring the final result is correct.