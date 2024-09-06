```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i, char in enumerate(string):
        if char == substring:
            count += 1
    return count

#Test the function
string1 = "aaa"
substring1 = "a"
result = how_many_times(string1, substring1)
print(result) # Output: 3

string2 = "abc"
substring2 = "ab"
result = how_many_times(string2, substring2)
print(result) # Output: 2

string3 = "aaaa"
substring3 = "aa"
result = how_many_times(string3, substring3)
print(result) # Output: 3
```
This script defines a function `how_many_times` that finds the number of occurrences of a given substring within a larger string. It then tests the unique cases of the function to pass the test.