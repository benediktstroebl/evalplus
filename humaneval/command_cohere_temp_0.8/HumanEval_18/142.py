Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases. """
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if string[i:j+1] == substring:
                count += 1
    return count

# Tests
def test_empty_string():
    assert how_many_times('', 'a') == 0

def test_missing_substring():
    assert how_many_times('aaa', 'b') == 0

def test_multiple_counts():
    assert how_many_times('aaaa', 'aa') == 3

def test_multiple_counts_with_overlaps():
    assert how_many_times('aaa', 'a') == 3

def test_single_count():
    assert how_many_times('aaaa', 'aaaa') == 1

def test_reverse_match():
    assert how_many_times('reverse', 'rev') == 1
```

The `how_many_times` function iterates through each possible interval within the main string, comparing it to the substring. The `tests` module validates the function against different cases.