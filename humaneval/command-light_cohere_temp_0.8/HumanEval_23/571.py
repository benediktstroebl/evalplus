```python
def strlen(string: str) -> int:
    return len(string)

# Test case 1
assertEqual(strlen(''), 0)

# Test case 2
assertEqual(strlen(''), 0)  

# Test case 3
assertEqual(strlen(''), 3)

# Test case 4
assertEqual(strlen('abc'), 3)

# Test case 5
assertEqual(strlen(''), equalityError())  # empty string raises 'TypeError'

# Test case 6
assertEqual(strlen('abc'), 3)  

# Test case 7
assertEqual(strlen('We Are Going To Solve Your Problem'), 13)  # long string
```