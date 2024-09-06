```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

#Test cases
string1 = "aaaa"aa"
string2 = "aaa"
string3 = "aaaaaaa"
string4 = ""
substring1 = "a"
substring2 = "aa"

print("Test case 1:", how_many_times(string1, substring1))
# should be 2
print("Test case 2:", how_many_times(string2, substring2))
# should be 1
print("Test case 3:", how_many_times(string3, substring1))
# should be 3
print("Test case 4:", how_many_times(string4, substring1))
# should be 0")
```
This code provides a function called **how_many_times()** that accepts two arguments: a string and a substring. It uses a approach to count the number of times the substring appears in the string, and returns the count. The function is then tested by passing different strings and substrings.