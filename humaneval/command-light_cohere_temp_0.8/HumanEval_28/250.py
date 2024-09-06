```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(''.join(string.join(strs))  for strs in strings)
```  This Python function, concatenate, takes a list of strings as an argument and concatenates them into a single string. It uses the string.join to iterate over the particular list of strings and the join() method to concatenate them. The result is a single string, which can be assigned to the variable answer. 

I have used type hints to indicate the expected argument type and the function return value is a string. This makes the function more readable and easier to understand.