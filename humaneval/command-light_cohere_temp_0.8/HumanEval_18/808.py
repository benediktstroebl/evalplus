```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test suite
def test():
    assert how_many_times('aaa', 'a') == 3
    assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('abcde', 'de') == 2
    assert how_many_times('123abc123', 'abc') == 4
    assert how_many_times('ABCDEFGHIJKLMNOPQRSTUV', 'DEF') == 8
test()
```
This code defines a function that counts the number of occurrences of a substring in a given string. It uses a basic loop to iterate through each character in the string and checks if the current character is equal to the given substring. The function then returns the count of occurrences.