```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count the occurrences of a given substring in the original string, 
    handling overlapping occurrences.
    """
    string: str - The original string 
    substring: str - The substring to search for
    """
    count = 0
    start = 0
    end = len(string) - 1

    while start <= end:
        current_index = string.find(substring, start, end)
        if current_index != -1:
            count += 1
            start = current_index + 1

    return count

# Test cases
string1 = "aaaaaa"aa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
print("result1:", result1)

string2 = "omalastest"
substring2 = "aaaa"
result2 = how_many_times(string2, substring2)
print("result2:", result2)

string3 = "hello world"
substring3 = "o"
result3 = how_many_times(string3, substring3)
print("result3:", result3)

``` 
This script defines a function called `how_many_times` that takes two arguments: a string and a substring. It then uses a strings and substrings, and the function returns the number of occurrences of the substring in the original string, handling overlapping occurrences.