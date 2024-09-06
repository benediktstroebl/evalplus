```python
def strlen(string: str) -> int:
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen(' ')), 1
assertEqual(strlen('abc')), 3
assertEqual(strlen('abcde')), 5
assertEqual(strlen('A")), 3
#
``` 
The length of the string is returned by the `strlen` function.  The script also includes some test cases to ensure the correctness of the function.