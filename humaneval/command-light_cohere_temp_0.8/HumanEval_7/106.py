```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Sample input and output 
strings = ["abc", "hello", "world", "level", "123"]
substring = "level" 

result = filter_by_substring(strings, substring)
print(result) # ['level']
``` 
This script defines a function called `filter_by_substring` that takes two parameters - a list of strings and a substring. The function uses a list comprehension to filter out only the strings from the input list that contain the given substring.