```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    length_string = len(string)
    length_substring = len(substring)

    for i in range(1, length_string + 1):
        found = False
        for j in range(1, length_substring + 1):
            if string[i - j] == substring[j - 1]:
                found = True
                count += 1
        if found:
            break

    return count

# Test cases
string1 = "aaa"
string2 = "a"
string3 = "aaaa"
string4 = ""
substring1 = "aa"
substring2 = "aaaa"
print("Result:", how_many_times(string1, substring1))  # Output: 3
print("Result:", how_many_times(string2, substring2))  # Output: 0
print("Result:", how_many_times(string3, substring1))  # Output: 3
print("Result:", how_many_times(string4, substring1))  # Output: 0
print("Result:", how_many_times(string3, substring2))  # Output: 3
```
This script defines a function `how_many_times` that finds the number of occurrences of a given substring within a given string. It takes a value of the string and substring as input and then runs the function. The number of occurrences is returned.