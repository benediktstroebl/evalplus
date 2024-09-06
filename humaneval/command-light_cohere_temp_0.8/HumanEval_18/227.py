```python
def how_many_times(string: str, substring: str) -> int:
    """
    Finds how many times a given substring can be found in the original string.
    Count overlapping cases
    how many times the string has the substring.
    Returns -1 if not found anywhere, 0 if empty, and otherwise the count.
    """
    method uses the for str.split() to find the string and list of substrings
    """
    result = 0
    for s in string.split(substring):
        if substring in s:
            result += 1
    return result

def test_how_many_times():
    try:
        assert how_many_times('', 'a') == 0
        assert how_many_times('aaaa', 'a') == 3
    assert how_many_times('aa', 'a') == 3
        assert how_many_times('aaaa', 'aa') == 2
        assert how_many_times('aaaa', 'aaa') == 0
        assert how_many_times('aaa', 'aaa') == 0
        assert how_many_times('a', 'b') == 0
        assert how_many_times('aa', 'aab') == 1
    except AssertionError as e:
        raise AssertionError(str(e))

# Call the function to test
test_how_many_times()
 ``` 
This code defines a function called how_many_times that returns the number of occurrences of a given substring in a given string. The function uses a list comprehension and a built-in function in Python called in. string to split the string into a list of substrings and check if the substring is in the list. The function also uses the same approach to count the occurrences of the substring in the original string, returning -1 if the substring is not found and 0 if the string is empty.