```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
print("Result1:", result1)

string2 = "The quick brown fox jumps over the lazy dog"
substring2 = " jump"
result2 = how_many_times(string2, substring2)
print("Result2:", result2)
```
The function how_many_times returns the count of occurrences of the substring in the string. It does so using a loop that checks each character in the string against the substring and increments the count if there's a match.