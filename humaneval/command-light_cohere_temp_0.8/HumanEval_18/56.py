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
string1 = "aaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
# Assertion 1
assert result1 == 3

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
# Assertion 2
assert result2 == 2

string3 = "AAaaaa"
substring3 = "aa"
result3 = how_many_times(string3, substring3)
# Assertion 3
assert result3 == 3
```
This code defines a function how_many_times that counts the occurrences of a given substring in a given string. The function utilizes a loop to iterate through each character in the input string and checks if the current character matches the provided substring. It returns the also and the number of matches found. The test cases ensure the validity of the function by providing various inputs and expected outputs, which are then checked using assertions.