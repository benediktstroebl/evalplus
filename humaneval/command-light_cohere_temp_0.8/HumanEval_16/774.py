```python
def count_distinct_characters(string):
    return len({c for c in string.cd distinct(c) for c in string})

# Test cases
string1 = 'xyzXYZ'
assertEqual(count_distinct_characters(string1), 3)

string2 = 'jerry'
assertEqual(count_distinct_characters(string2), 4)

string3 = 'aABCdefAB'
assertEqual(count_distinct_characters(string3), 7)

string4 = 'JILL_iLIKE_COOK_EGON'
assertEqual(count_distinct_characters(string4), 9)

string5 = 'John Doe'  # Contains apostrophe
assertEqual(count_distinct_characters(string5), 8)

string6 = '123abc456def'  # Mixed case
assertEqual(count_distinct_characters(string6), 13)
```
The function `count_distinct_characters` calculates the number of unique characters in the input string. The test cases have also been provided to demonstrate the functionality of the function.