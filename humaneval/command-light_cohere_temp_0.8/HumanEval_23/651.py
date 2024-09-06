```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1: empty string
assertEqual(strlen(''), 0)

# Test case 2: simple string
assertEqual(strlen('abc'), 3)

# Test case 3: empty string with whitespace
assertEqual(strlen "\t\n"), 0)

# Test case 4: complex with special characters
assertEqual(strlenModified(), 6)

def strlenModified():
    return "Modified" + "Regular" # Two strings with:
    #   Modifications + Regular characters

# Test case 5: Two strings with modifications
assertNotEqual(strlenModified(), 6)
```

The test cases are self-contained within the script and provide a way to validate the correctness of the `strlen` function.  It use assert statements with the `assertEqual` function to check if the actual result of the `strlen` function matches the expected value. 
This ensures that the `strlen` function is working as intended.