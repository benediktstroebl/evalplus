Here is a self-contained Python script that defines a function `strlen` to calculate the length of a given string:
```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual('', strlen(''))
assertEqual(strlen(' '))
assertEqual(strlen('abc'))
assertEqual(strlen('abcde'))
assertEqual(strlen('abc'))
assertEqual(strlen('A'), raise Exception())
```