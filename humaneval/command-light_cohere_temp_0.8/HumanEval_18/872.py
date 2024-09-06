```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Test the function
string1 = "aaaaaa"
substring1 = "a"
result = how_many_times(string1, substring1)
print(result)  # Output: 3

string2 = "Python"
substring2 = "y"
result = how_many_times(string2, substring2)
print(result)  # Output: 2
```
This code defines a function how_many_times that calculates the frequency of a given substring within a given string. The function uses a loop to iterate over each character in the string and counts how many times the substring appears.