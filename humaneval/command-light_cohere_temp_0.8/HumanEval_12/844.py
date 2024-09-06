Here is a self-contained Python script that solves the problem of finding the longest string in a list of strings:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # Check if the list is empty
    if not strings:
        return None
    
    # Initialize the variable to store the longest string
    longest_str = strings[0]
    
    # Iterate through the list
    for string in strings:
        # Compare the length of the current string with the previous longest
        if len(string) > len(longest_str):
            longest_str = string
    
    return longest_str

# Example usage
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest string:", longest_result)
```

This code defines a function called `longest` that takes a list of strings as input and returns the longest string from that list. The function first checks if the list is empty and returns `None` in such case. Then, it initializes the variable `longest_str` to the first string in the list and iterates through the list, comparing the length of each string with the previous longest one and updating `longest_str` accordingly. The function returns the value of `longest_str` as the answer. 

The output of this code will be the longest string in the list of strings provided.