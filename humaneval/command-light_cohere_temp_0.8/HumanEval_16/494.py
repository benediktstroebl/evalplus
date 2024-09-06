Here's a self-contained Python script that defines a function count_distinct_characters that calculates the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    """ 
    Count the number of distinct characters in a given string, 
    regardless of case. 
    Returns: number of distinct characters.
    """ 


    Args: 
    string (str): A string 
	) 
	Returns: 
    int: Number of distinct characters 
    """
    # Convert the string to lowercase to make case irrelevant
    string = string.lower()
    string 
    # Split the string into individual characters 
    char_list = string.split()
    unique = len([char for char in char_list if char.isalpha() and distinct])
    distinct_characters = unique
	return distinct_characters
``` 
The function has been expanded to better suit the prompt and test case.