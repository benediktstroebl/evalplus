```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaa"
string2 = "aaaa"
string3 = "aaaaaa"
print(how_many_times(string1, string2))  # Output: 3
print(how_many_times(string1, string3))  # Output: 0
print(how_many_times(string2, string3))  # Output: 2
print(how_many_times("", "a"))  # Output: 0
print(how_many_times("", "aaaa")) # Output: 6)
``` 
This function defines a function that takes two arguments: a string and a substring. The function uses a loops through each character in the string and counts how many times the substring appears.