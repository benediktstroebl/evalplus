```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.
    """
    string = string.split()
    string = [i for i in string if i == substring]
    return len(string)

# Test cases
test_many_times = []
test_many_times.append(["aa", "aaa"])
test_many_times.append(["abb"], "ab")
test_many_times.append(["abc", "abc"])
test_many_times.append(["abcd"], "abcd")
test_many_times.append(["abcf"], "abc")
test_many_times.append(["ab", "ab"]*2)

test_many_times.run(map(lambda x: how_many_times(*x), test_many_times))

print("Test cases passed!")
```