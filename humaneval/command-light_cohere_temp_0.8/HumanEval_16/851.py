```python
def count_distinct_characters(string: str):
    return len([char for char in string.str.count(char.lower()) for char in string if char not in set(char.isalpha()))

# Run tests
test_count_distinct_characters('xyzXYZ') assert 3 == count_distinct_characters('xyzXYZ')
test_count_distinct_characters('Jerry') assert 4 == count_distinct_characters('Jerry')
``` 
This function, `count_distinct_characters`, takes a string as input and returns the count of distinct characters in that string, regardless of case. This is achieved using a set of all characters in the string, filtering out the duplicates, and counting the remaining characters. The function also converts all characters to lowercase before performing the count to ensure that it ignores case.