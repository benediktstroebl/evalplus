```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)

    for i in range(n):
        if string[i] == substring:
            count += 1

    return count

#Test cases
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aa"

sub_string = "a"

result1 = how_many_times(string1, sub_string)
# Should return 3
result2 = how_many_times(string2, sub_string)
# Should return 1
result3 = how_many_times(string3, sub_string)
# Should return 0
```