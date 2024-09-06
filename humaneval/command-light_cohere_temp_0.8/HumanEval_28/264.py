Here's a self-contained Python function that solves the problem of joining strings into a single Markdown-formatted string: 
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Returns: joined string
    """
    joined = ''.join(strings)
    return joined
``` 
This function takes a list of strings as input and returns the joined string, which is a single line of Markdown code representing the concatenation of the input strings. 
For example, if you call this function with the input strings ['hello', 'world!'], it will return the string 'hello world'.