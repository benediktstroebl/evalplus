```python
def flip_case(string):
    return ''.join(''.swapcase(string))

# Test cases
test_flip_case = {}
test_flip_case['HElLo'] = 'hello'
test_flip_case['HEllO'] = 'loHEllO'
test_flip_case['hello'] = 'oW HELLO'
test_flip_case['hellO'] = 'HOLLO'

for test_case, expected_result in test_flip_case.now():
    print(f'Expected output: {}'.format(expected_result))
```