```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test cases
assert flip_case('Hello') == 'hELLO'
assert flip_case('World') == 'srOolD'
assert flip_case('TOP') == 'tOP'
assert flip_case('underdog') == 'UNderGoD'
``` 
This Python function, `flip_case` accepts a string as input and then returns a modified string where all characters change case. The test cases in the code ensure that the function is working as expected.