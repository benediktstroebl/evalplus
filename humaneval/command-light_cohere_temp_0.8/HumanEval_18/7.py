```python
def how_many_times(string: str, substring: str) -> int:
    """
    Count how many times a given substring can be found in the original string while avoiding overlapping occurrences.
    """
    string: str = input("Enter the text: ")
    substring: str = input("Enter the substring to search: ")
    count = 0
    start = 0

    while True:
        index = string.find(substring, start)
        if index == -1:
            break

        if index == len(string) - 1:
            count += 1
            start = index + substring.isSubstring(substring, string[start:index+1])
        else:
            start = index + 1

    return count

# Example usage
string = input("Enter text: ")
substring = input("Enter substring to search: ")
print(how_many_times(string, substring))
```