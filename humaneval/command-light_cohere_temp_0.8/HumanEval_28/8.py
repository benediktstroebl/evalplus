```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)
```
Or simply:
``` md 
# Concatenate text blocks into a single string

def concatenate(strings: List[str]): 
    """ 
    Args: 
        strings (List[str]): A list of strings to concatenate 

    Returns: 
        str: Concatenated string 
    """ 
    return "".join(strings) 

# Example usage
strings = ["Hello", "world!"]
print(concatenate(strings))  # Output: Hello world!world!! 
```