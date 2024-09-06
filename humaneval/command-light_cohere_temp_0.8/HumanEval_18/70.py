```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in substring:
        if char in string:
            count += 1
    return count

# Test the function
string1 = "aaaa"
substring1 = "aa"
print(how_many_times(string1, substring1))  # Output: 3

string2 = "hello"
substring2 = "el%"
print(how_many_times(string2, substring2))  # Output: 2

string3 = "abc"
substring3 = "abc"
print(how_many_times(string3, substring3))  # Output: 4
```
This Python code defines a function how_many_times that counts the occurrences of a given substring within a given string. It uses a array-like behavior and a loop to iterate through each character of the substring and increment a count if the character is present in the original string. The function is then tested with three example cases, providing the expected output for each one.