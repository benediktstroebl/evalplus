```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Function to find how many times a given substring can be found in the original string.
    """ 
    Count_overlapping_count = 0 
    for i in range(len(string)):
        if string[i] == substring:
            if substring == string[i:]:
                continue
            else:
                how_over = 0
                j = i
                while j < len(string) and string[j] == substring:
                    how_over += 1
                    j += 1
                count_overlapping = how_over
                if count_overlapping == 0:
                    break
        return len(string) - count_overlapping
    return None
def test_function():
    string = "aaaaaaa"
    substring = "a"
    result = how_many_times(string, substring)
    assert result == 3
    substring = "abc"
    result = how_many_times(string, substring)
    assert result == 3
    substring = "foo"
    result = how_many_times(string, substring)
    assert result == 0
    return True
```