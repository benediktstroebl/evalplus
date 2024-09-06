```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string):
            if char == substring):
        return i + 1
    return 0

# Test the function
test = unittest.py()
from funct_functions import how_many_times

test.how_many_times("aaaaaa", "aa")
test.run(' how_many_times(""))
test.run(' how_many_times("abcd", "ab")')
test.run(' how_many_times("abcdaaaa", "aa")')
``` 
This code defines a function called `how_many_times`, which accepts two parameters: a string and a substring. The function returns the number of times the substring appears in the string, and the function counts the number of occurrences while avoiding duplication.