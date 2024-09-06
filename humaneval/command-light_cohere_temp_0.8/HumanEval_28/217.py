```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    
    Returns:
        str: Concatenated string
    """
    return ''.join(strings)

# Test the concatenate function with various inputs
test_concatenate = [
    'a'.concatenate(['b', 'c']),
    [], ''.join(test_concatenate)
]
print(test_concatenate)
 ```