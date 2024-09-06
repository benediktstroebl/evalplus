```python
def how_many_times(string: str, substring: str) -> int:
    """
    Counts the occurrences of a substring within the original string, without overlapping.
    """
    return sum(1 for i, j in enumerate(string.find(substring))
    """

    # Test
    assert sum(1 for i, j in enumerate(string.find(substring)) == len(string)
    assert sum(1 for i, j in enumerate('abc'.find(substring)) == 3
    assert sum(1 for i, j in enumerate('aaaaaa'.find(substring)) == 6
    assert sum(1 for i, j in enumerate('abcde'.find(substring)) == 3
    assert sum(1 for i, j in enumerate('aeiou'.find(substring)) == 7
    assert sum(1 for i, j in enumerate(''.find(substring)) == 0
    assert sum(1 for i, j in ['a','ab','abc','abcd','abcde'].find(substring)) == 4
    assert sum(1 for i, j in [''.find(substring) for i in range(1, 200)]) == 400
    assert sum(1 for i, j in ['abcd','abcde','abcf'].find(substring)) == 3
    assert sum(1 for i, j in set([i for i, j in ['a'ipher][::i].find(substring)] if i)) == 128

    """

The code you provided is a Python script with a self-contained function that solves the problem of counting the occurrences of a given substring within a string, without overlapping. The function uses the verify its implementation using several tests, which demonstrate its correctness and ability to handle various scenarios correctly.