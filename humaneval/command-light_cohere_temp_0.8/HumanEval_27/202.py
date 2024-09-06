```python
def flip_case(string):
    return ''.join_lowercase(string) if string.isalpha() else string.lower()
lower() if string.isupper() else string.isalpha()


def test_flip_case():
    assert flip_case('Hello') == 'H EllO'
    assert flip_case(' Atomic') == ' atM icT'
    assert flip_case(' lower') == ' Lou er'
    assert flip_case('tomorrow') == 'toArrayrd'

if __name__ == "__main__":
    test_flip_case()
``` 
This function `flip_case` takes a string as input and converts its characters to their corresponding case, depending on input. The test function ensures that the function behaves as expected.