```python
def strlen(string: str) -> int:
    """ Returns length of the given string"""
    return len(string)

#Test string length function
assertEqual(strlen(''), 0)
assertEqual(strlen('')), 0, "empty string should return 0")
assertEqual(strlen('abc')), 3, "single character string should return 3")
assertEqual(strlen('hello world')), 13, "longer string should return correctly")

```