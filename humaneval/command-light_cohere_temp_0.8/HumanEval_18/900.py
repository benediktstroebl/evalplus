```python
def how_many_times(string: str, substring: str) -> int:
    """ 
    Returns the number of occurrences of a substring in the original string.
    """ 
    if not substring.isubstring(substring):
        raise ValueError("Substring must be a proper substring of the string")
    return sum(1 for x in string.isubstring(x) if x == substring)

test_how_many_times = []
test_how_many_times.append([string_list(["aa", "aaa", "aaaa"]), "aa")
test_how_many_times.append([string_list(["a", "ab", "ac"], "a"))
test_how_many_times.append([string_list(["ab", "abc"], "ab"))
test_how_many_times.append([string_list(["abcd"], "abcd"), 2)

print(how_many_times("aaaa", "aa"))
```