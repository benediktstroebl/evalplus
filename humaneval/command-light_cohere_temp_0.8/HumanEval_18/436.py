```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Testing the function
string1 = "aaaa"
string2 = "aaa"
substring1 = "aa"
substring2 = "aaa"

print(how_many_times(string1, substring1))  # Output: 3
print(how_many_times(string1, substring2))  # Output: 0
print(how_many_times(string2, substring1))  # Output: 3
print(how_many_times(string2, substring2))  # Output: 2
```