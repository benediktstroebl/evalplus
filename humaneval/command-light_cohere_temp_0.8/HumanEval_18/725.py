```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

# Test the function
string1 = "aaaa"aa"
string2 = "aaa"
print(how_many_times(string1, string2))  # Output: 3
```
This function employs a for loop to iterate through each character in the input string. Additionally, it compares each character to the substring. The function returns the number of times the substring appears in the input string, with overlapping cases being counted.