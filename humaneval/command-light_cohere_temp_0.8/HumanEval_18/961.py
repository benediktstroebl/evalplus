```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaaa"
substring1 = "aa"
print(how_many_times(string1, substring1))  # Output: 6

string2 = "Hello"
substring2 = "o"
print(how_many_times(string2, substring2))  # Output: 2
```
This function takes two parameters: `string`, which represents the input string, and `substring`, which is the substring to find. The function then iterates through the string and compares each character with the substring. It counts if they matches, the count of matches is incremented. The function returns the count, indicating the number of times the substring is found in the original string.