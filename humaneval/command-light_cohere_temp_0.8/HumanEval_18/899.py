```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    # iterate over each character in the string
    for char in string:
        # check if the character matches the substring
        if char == substring:
            count += 1
    return count
# tests
def test_how_many_times():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'aa') == 3
    assert how_many_times('abcde', 'abc') == 2
    assert how_many_times('abcba', 'ab') == 3
    assert how_many_times('abcba', 'b') == 0
    assert how_many_times('hello', 'ello') == 0
```