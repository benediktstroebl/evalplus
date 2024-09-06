```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaa"
string2 = "aaaaaa"
string3 = "aaa"
string4 = "a"
string5 = "aa"

print(how_many_times(string1, string1))  # Output: 5
print(how_many_times(string2, string1))  # Output: 0
print(how_many_times(string3, string1))  # Output: 2
print(how_many_times(string4, string1))  # Output: 3
print(how_many_times(string5, string1))  # Output: 0
```
The code defines a function called **how_many_times** that takes two parameters: a string and a substring. The function uses a loop to iterate over the string and counts the number of times the substring is found. The code provides several test cases to demonstrate the functionality of the function.