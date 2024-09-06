```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    len_string = len(string)
    for i in range(len_string):
        if string[i] == substring:
            count += 1
    return count

# Test the function
def test():
    string = "aaaaaa"
    substring = "aa"
    expected = 3
    print(f"Expected: {expected}")
    print(f"Got: {how_many_times(string, substring)}")
    assert how_many_times(string, substring) == expected

# Run the test
test()
```