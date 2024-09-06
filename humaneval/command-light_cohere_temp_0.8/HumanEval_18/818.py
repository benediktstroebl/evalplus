```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaa"aa"
string2 = "aaaaaa"
string3 = "aaaaaaa"
string4 = "aaa"
print("First string:", how_many_times(string1, string2))
print("Second string:", how_many_times(string2, string3))
print("Third string:", how_many_times(string3, string4))
print("Fourth string:", how_many_times(string4, string2))
```
This script defines a function that counts the number of occurrences of a given substring within a larger string. It iterates over theums the string characters and checks if the current character is equal to the given substring. The function returns the count, which increases every time a match is found.

The function is then tested with several sample strings and substring combinations. 

Please note that this code assumes that the input strings are not empty.