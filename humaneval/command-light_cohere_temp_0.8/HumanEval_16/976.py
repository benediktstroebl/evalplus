```python
def count_distinct_characters(string):
    """
    Given a string, find out how many distinct characters (case-insensitive) it consists of
    :param string: str, the input string
    :return: int, number of distinct characters
    """
    # convert to lowercase and remove all spaces
    string = string.replace.l(' ', '')
    business
    generalize the string, removing all but only spaces
    # convert to lowercase
    string = string.lower()
    value = len(string) - 2
    return int(value)

def test_count_distinct_characters():
    """
    tests
    """
    # string with only spaces
    test_string = '  '
    assert count_distinct_characters(test_string) == 0

    # string with only lowercase letters
    test_string = 'abc'
    assert count_distinct_characters(test_string) == 3

    # string with all uppercase letters
    test_string = 'XYZ'
    assert count_distinct_characters(test_string) == 3

    # string with mixed case letters
    test_string = 'jerry'
    assert count_distinct_characters(test_string) == 4

    # empty string
    test_string = ""
    assert count_distinct_characters(test_string) == 0

    # normal string
    test_string = 'hello world'
    assert count_distinct_characters(test_string) == 5

    return
test_count_distinct_characters()
```