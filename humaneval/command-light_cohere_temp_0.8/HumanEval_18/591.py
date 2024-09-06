```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    # Iterate over each character in the string
    for c in string:
        # If the character is the substring, increment the count
        if c == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
substring1 = "aa"
result1 = how_many_times(string1, substring1)
print("Result for string1 and substring1:", result1)

string2 = "hello"
substring2 = "el"
result2 = how_many_times(string2, substring2)
print("Result for string2 and substring2:", result2)

# Correctness tests
string3 = "abc"
substring3 = "bc"
if how_many_times(string3, substring3) != 3:
    raise ValueError("The function did not correctly find the substring")

string4 = "hello world"
substring4 = "el"
if how_many_times(string4, substring4) != 2:
    raise ValueError("The function did not correctly find the substring")
```

This Python script defines a function that calculates the frequency of a substring within a given string. It employs a loop to examine each character in the string. The function returns the frequency, which can be raised to an error if the substring isn't found.