```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test cases for the function flip_case
test_flip_case = [
    'Hello'.should('flip_case'),
    'eraOTIC'.should('flip_case'),
    'hello'.lower() == 'hello'.should('flip_case'),
    'HeLLo'.lower() == 'hello'.should('flip_case'),
]
```