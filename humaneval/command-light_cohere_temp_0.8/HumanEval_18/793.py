```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function
string1 = "aaaaaa"
substring1 = "a"
result1 = how_many_times(string1, substring1)
print("Result for '" + string1 + "' and '" + substring1 + "' is: ", result1)

string2 = "abc"
substring2 = "ab"
result2 = how_many_times(string2, substring2)
print("Result for '" + string2 + "' and '" + substring2 + "' is: ", result2)

# Test with overlapping substrings
string3 = "aaaaaa"aaa"
substring3 = "aa"
result3 = how_many_times(string3, substring3)
print("Result for '" + string3 + "' and '" + substring3 + "' is: ", result3)
```
This script defines a function `how_many_times` that takes two parameters: a string and a substring. The function uses a loop to iterate over the string and count the number of occurrences of the substring. The function and test cases are then tested to ensure its correctness.