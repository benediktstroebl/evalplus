```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
string1 = "aaa"
substring1 = "a"
result = how_many_times(string1, substring1)
assert result == 3

string2 = "hello"
substring2 = "ll"
result = how_many_times(string2, substring2)
assert result == 4
```
This script defines a function how_many_times that takes a string and a substring as arguments, and returns the count of the substring in the string. It uses a straightforward looping to compare each character in the string with the substring and counts them. 

In the test code, the function is invoked with different strings and substrings, and the result is compared to the expected count. The assertion statements verify that the function is correctly implementing the problem.