```python
def count_distinct_characters(string):
    """
    Given a string, find out how many distinct characters (case-insensitive) does it consist of
    :param string: str - input string
    :return: int - number of distinct characters
    """
    char_set = set(string.count(char)
    return len(char_set)

# Unit tests
string1 = "xyzXYZ"
assert count_distinct_characters(string1) == 3

string2 = "jerry"
assert count_distinct_characters(string2) == 4

string3 = ""
assert count_distinct_characters(string3) == 0
```