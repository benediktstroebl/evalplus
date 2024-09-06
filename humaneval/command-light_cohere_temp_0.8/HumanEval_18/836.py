```python
def how_many_times(string: str, substring: str) -> int:
    """
    Function that counts the number of occurrences of a substring in the original string.
    >>> how_many_times('aaaaaa', 'aa')
    3
    """
    count = 0
    substring_len = len(substring)
    for i in range(len(string)):
        if string[i:i+substring_len] == substring:
            count += 1
    return count

#Test cases
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
print("Result for string1:", result1)

string2 = "hello world"
substring2 = "o"
result2 = how_many_times(string2, substring2)
print("Result for string2:", result2)

string3 = "This is a test"
substring3 = "ass"
result3 = how_many_times(string3, substring3)
print("Result for string3:", result3)
```