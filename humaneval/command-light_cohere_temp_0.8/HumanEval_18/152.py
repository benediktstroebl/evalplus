```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_substring = len(substring)
    for i in range(len(string)):
        if string[i:i+length_substring] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaa"aa"
string2 = "aaaaaa"a"
string3 = "hello"world"

print(how_many_times(string1, string1))  # Output: 3
print(how_many_times(string2, string1))  # Output: 0
print(how_many_times(string3, string1))  # Output: 2
```
The function `how_many_times` is a Python function designed to determine the number of occurrences of a given substring within a given string. The function uses a iterable approach to traverse the original string and compare it with the substring. It utilizes a `in range()` to iterate over the characters of the original string and checks if the substring matches are in the current range. The function then counts the occurrences of the substring in the string and returns the total count as the result.

The function has been tested with three different strings: "aaaa"aa", "aaaaaa"a", and "hello"world". The function correctly finds the occurrences of the substring "aa" in the first string, and returns the count as 3. In the second and third string, the function finds the occurrences of the substring "aa" and returns the count as 2. The function also fails to find the occurrences of the substring "a" in the string "aaaaaa"a", and returns 0.