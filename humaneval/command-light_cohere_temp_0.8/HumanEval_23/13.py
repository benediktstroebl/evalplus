```python
def strlen(string: str) -> int:
    return len(string)

#Test case 1: String is empty
assert(strlen('') == 0)

#Test case 2: String contains only one character
assert(strlen('abc') == 3)

#Test case 3: String contains more than one character
assert(strlen('hello')) == 5
```