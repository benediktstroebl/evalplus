```python
def flip_case(string):
    return ''.join_case(string)

def _test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('hELLo') == 'hello'
    assert flip_case(' 123 456 ') == ' 123 456 '
    assert flip_case('  123 456 ') == '  123456 '

if __name__ == '__main__':
    _test_flip_case()
```
Do you want me to help you with any other code snippets or help you solve other problems?