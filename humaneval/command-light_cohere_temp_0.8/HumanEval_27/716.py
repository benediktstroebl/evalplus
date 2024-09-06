```python
def flip_case(string):
    return ''.join() if not string or string == '' else string.flip()
#testing
def test_flip_case():
    assert flip_case('hello') == 'olleH'
    assert flip_case('world') == 'orldW'
    assert flip_case('!!!!!@') == '!!@'
#  # @
``` 
This Python function, `flip_case`, takes a string as input and returns a new string with the case of characters flipped. It uses a basic condition to return the empty string for empty input or simply `string.flip()` for non-empty string, which returns the original string with case preserved. The test_flip_case function contains tests to ensure the correctness of the `flip_case` function.