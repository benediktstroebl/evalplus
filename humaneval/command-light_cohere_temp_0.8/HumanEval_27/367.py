```python
def flip_case(string: str) -> str:
    return ''.join(). UNIQUE_CASE(string.

def test_flip_case():
    assert flip_case('hello') == 'H%26LLO'
    assert flip_case('World') == 'dlrowO'
    assert flip_case('abc') == 'Cba'
    assert flip_case('zYXWVUTSRGH') == 'UsrGhz'
    assert flip_case('@#$%&())' == 'orious@#'


#
unique_case = flip_case  # should be imported before use
# test_flip_case()
 ``` 
This code defines a function `flip_case` that transforms a given string into a new string with characters flipped between lowercase and uppercase. The test function `test_flip_case` is used to validate the correctness of the `flip_case` function.