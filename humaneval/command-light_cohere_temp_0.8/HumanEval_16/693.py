```python
def count_distinct_characters(string):
    """
    Returns the count of distinct characters in the string, regardless of case.
    """
    string = 'xyzXYZ'
    return len([char for char in string.char if char.isnt distinct()])
 distinct()

def test_count_distinct_characters():
    """
    Test case 1
    >>> test_count_distinct_characters('xyzXYZ')
    3
    Test case 2
    >>> test_count_distinct_characters('jerry')
    4
    """
    print(count_distinct_characters('xyzXYZ'))
    print(count_distinct_characters('jerry'))

if __name__ == "__main__":
    test_count_distinct_characters()
 ```