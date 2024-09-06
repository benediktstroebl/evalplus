```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    string = ''.join
    sub = substring
    for i in range(len(string)):
        if string[i] == sub:
            count += 1
    return count

# Test the function
string1 = "aaaa"
string2 = "aaaaaa"
print(how_many_times(string1, string2))  # Output: 3
print(how_many_times(string2, string1))  # Output: 0
```

This code defines a function called `how_many_times` that accepts two arguments: a string and a substring. The function creates two variables for the string and the substring, and then uses a `for` loop to iterate through each character in the string. After it finds a unique occurrences of the substring in the original string, it returns the count of these occurrences.