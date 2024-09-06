```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases for function
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)
# Test case with empty input
strings = []
substring = "a"
result = filter_by_substring(strings, substring)
print(result)
``` 
This Python code defines a function **filter_by_substring** that takes two arguments: a list of strings **strings** and a substring **substring**. The function returns a new list containing only the elements from the original list that contain the specified substring. The code then provides several test cases to demonstrate the functionality of the function. It successfully filters the for the input strings that do not contain the substring, and an empty input list.