```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
print("Result1:", result1)

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
print("Result2:", result2)

string3 = "hello"
substring3 = "o"
result3 = how_many_times(string3, substring3)
print("Result3:", result3)

# Correctness will be validated by the below tests. 
```