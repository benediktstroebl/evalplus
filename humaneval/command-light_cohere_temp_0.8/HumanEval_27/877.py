```python
def flip_case(string):
    return ''.join_lowercase(string)[::-1]

def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('HELLO') == 'hello'
    assert flip_case('Hello World!') == 'dlroW olleW'
    assert flip_case(' abc def ghi') == ' Defg abc'
    assert flip_case('@#$%^&*()') == 'zies A ttu uro'
```
The `flip_case` function takes a string as input and returns a new string where the first character of each line is reversed. This is can be achieved using the `string.join_lowercase()` method that turns a string to lowercase and then reverse it.