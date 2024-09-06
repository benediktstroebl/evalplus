Here's the self-contained Python script with the function that solves the problem:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    n = len(string)
    m = len(substring)
    for i in range(n):
        if string[i] == substring:
            count += 1
    return count

# Test the function with some examples
string1 = "aaaaaa"
string2 = "aaaa"
string3 = "aaaaaaa"
string4 = "a"
string5 = "aa"

print("String:", string1, string2, string3, string4, string5)")
print("SubString:", string2, string3, string4, string5)")
print("How Many Times:", string1, string2, string3, string4, string5, subString)")
print("Count:", how_many_times(string1, string2), how_many_times(string1, string3), how_many_times(string1, string4), how_many_times(string5, subString)")

```

The function `how_many_times` accepts two parameters: a string and a substring, and it returns an integer indicating the frequency of the substring in the original string. 

The function uses a loop to iterate through each character in the input string and counts the number of occurrences of the substring.