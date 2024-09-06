Here's a self-contained Python script that defines a function how_many_times that finds the number of occurrences of a substring within a given string.

```python
import string

def how_many_times(string: str, substring: str) -> int:
    count = 0
    length = len(substring)
    for i in range(len(string)):
        if string[i:i+length] == substring:
            count += 1
    return count

# Test cases
string1 = "aaaaaa"
string2 = "aaa"
string3 = "aaaa"

assert how_many_times(string1, string1) == 3
assert how_many_times(string2, string2) == 3
assert how_many_times(string3, string3) == 3
```
This script defines a function `how_many_times` that calculates the number of occurrences of a given substring within a main string. The function iterates through the string character by character and checks if the substring is currently being matched, if so, it increments a count. 

The test cases validate the function's behavior for different input scenarios.