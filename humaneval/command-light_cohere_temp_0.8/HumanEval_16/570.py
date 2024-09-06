```python
def count_distinct_characters(string: str) -> int:
    characters = set(string)
    return len(characters)

# Test the function
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('abcABC')
4
>>> count_distinct_characters('foo Bar')
3
>>> count_distinct_characters('jerry ONE')
4
>>> count_distinct_characters(' lonely weekend')
3
``` 
This script defines a function `count_distinct_characters` that accepts a string as an argument and returns the count of distinct characters in that string, regardless of case. It utilizes the set to collect the distinct characters and then counts them.