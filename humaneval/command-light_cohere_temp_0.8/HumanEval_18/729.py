```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

# Example test cases
string1 = "aaaa"
string2 = "aaaaaa"
string3 = "aaa"
string4 = ""

for idx, string in enumerate(['string1', 'string2', 'string3', 'string4'], start=1):
    sub = 'aaaa'
    print(f'how_many_times("{string}", {sub})'  # Output: 3')

```
This function, `how_many_times`, finds the count of occurrences of a given substring within a given string. It utilizes a necessary loop to iterate through the string and check if each character matches the substring. The function returns the count of characters that match the substring.