Here's the self-contained Python function that filters a list of strings based on a given substring:
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains.find(substring)]
 filter_by_substring([], 'a') # [()] will return an empty list.
```
This function takes two parameters: a list of strings and a substring string. It returns a filtering the string list based on whether the substring is present in each string. 

Here's a simple example of how to use the function:
```python
my_strings = ['abc', 'bacd', 'cde', 'array', 'hello']
my_substring = 'a'
filtered_strings = filter_by_substring(my_strings, my_substring)
print(filtered_strings) 
```

This will print the list of strings that contain the substring 'a': ['abc', 'bacd', 'array'].