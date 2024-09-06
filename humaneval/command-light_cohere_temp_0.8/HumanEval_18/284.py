```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)

    for i in range(n):
        if string[i:i+m] == substring:
            count += 1

    return count

# Test the function
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
print("Result1:", result1)

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
print("Result2:", result2)

```
This code defines a function called `how_many_times` that takes two parameters: a string and a substring. It then returns an number of times the substring appears in the original string, counting overwriting cases. The function uses a inner loop to iterate through the string and check if the substring appears at that position or later in the string. The function then returns the count of how many times the substring appears in the original string.