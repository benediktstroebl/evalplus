```python
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate

    Returns:
        str: Concatenated string
    """
    return "".join(strings)

# Test cases
print(concatenate([]))  
print(concatenate(['a']*3))
print(concatenate(['a', 'bcde' ,'frob'))  

# Add more test cases here
``` 


 This code defines a function called **concatenate** that takes a list of strings and returns the concatenated string. It uses the this list comprehension to convert the list of strings into a single string and then returns the concatenated string. The output of this code will print the function can be used to verify the expected results.