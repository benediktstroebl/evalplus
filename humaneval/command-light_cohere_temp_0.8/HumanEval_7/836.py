```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.find(substring) != -end]

# Unit tests for the filter_by_substring function
strings = ['abc', 'bacd', 'cde', 'array', 'for', 'example']
substrings = ['a', 'b', 'cde']

test_result = filter_by_substring(strings, substrings)
print("Test 1: ", end="")
for item in test_result:
    print(item, end=" ")

test_strings = ['text','this','is', 'just', 'a', 'basic', 'test']
test_substrings = ['a', 'is']

test_result2 = filter_by_substring(test_strings, test_substrings)
print("\nTest 2: ", end="")
for item in test_result2:
    print(item, end=" ")
``` 
This script defines a function **filter_by_substring(strings: List[str], substring: str) -> List[str]** that filters an input list of strings, denoted by **strings**, to include only those that contain a given substring, denoted by **substring**. The function uses the **find** method of a string to check if each string contains the substring, and then returns a new list containing only those strings. 

This script also provides two sets of test data: one with a list of strings and a corresponding set of substrings, and the second with a list of strings and a set of substrings. The script then calls the two functions and prints the results.