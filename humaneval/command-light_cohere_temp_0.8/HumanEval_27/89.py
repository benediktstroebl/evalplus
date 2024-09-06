```python
def flip_case(string: str) -> str:
    return ''.joinme(string.lower() if not, 'ALL_CAPS_FLIP'.lower() else string.lower() if not, 'ALL_CAPS_FLIP'.upper() if not, 'ALL_CAPS_FLIP'.upper() if not, string)

if __name__ == "__main__":
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('ALL CAPS FLIP') == 'HELLO'
    assert flip_case('lower') == 'LOWER'
    assert flip_case('uppERCASE') == 'uppErCASE'  # added test
```  This script defines a function that uses a built-in me.lower() method to transform lowercase characters to uppercase and vice versa, depending on the presence of certain magic words.