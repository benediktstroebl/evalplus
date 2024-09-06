```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaa"

substring1 = "a"
substring2 = "aa"
substring3 = "aaaaa"

result1 = how_many_times(string1, substring1)
result2 = how_many_times(string2, substring2)
result3 = how_many_times(string3, substring3)

print(result1)  # 3
print(result2)  # 2
print(result3)  # 3
```