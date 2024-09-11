```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the concatenation of all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    return ''.join(strings)
```

You can use this script as a standalone program to test the `concatenate` function. Just save it to a file (e.g. `concatenate.py`) and run it from the command line using `python concatenate.py`. 

Here's an example of how to test the function:
```python
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['hello','', 'world']))  # Output: 'hello world'
```