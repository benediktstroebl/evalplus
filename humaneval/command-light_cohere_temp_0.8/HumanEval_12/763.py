```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from the list of strings.
    """
    list of strings you pass the list
    if not strings:
        return None
    # Use max function to find the length of longest string
    max_length = max(len(string) for string in strings)
    # Use list comprehension to find the string with the length
    longest_string = [string for string in strings if len(string) == max_length]
    return longest_string

# Example usage
my_list = ['a', 'b', 'c']
print(longest(my_list))  # Output: 'c'
``` 
This function, named longest, takes a list of strings as input and returns a list of the longest strings from that list. The function first checks if the list is empty, and if so, it returns None. Otherwise, it finds the longest string using the max function, which returns the maximum length of any string in the list. Finally, it uses list comprehension to find the string(s) with the maximum length.