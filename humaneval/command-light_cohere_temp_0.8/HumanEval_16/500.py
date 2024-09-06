```python
def count_distinct_characters(string: str) -> int:
    return len(string)

# Testing the function
string1 = 'xyXyzXYZ'
string2 = 'jerry'
string3 = 'jRey'

assert count_distinct_characters(string1) == 3
assert count_distinct_characters(string2) == 4
assert count_distinct_characters(string3) == 5
``` 
This code defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters in that string, regardless of case. It uses the straightforward logic of counting the number of characters and returning the total count as the result.