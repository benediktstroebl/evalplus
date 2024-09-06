def concatenate(input_list: List[str]) -> str:
    """
    This function takes in a list of strings and concatenates them into a single string, 
    separating each string with an empty space, and ignoring empty strings within the list. 
    Returns an empty string if the input list is empty.
    
    Args:
        input_list (list): A list of strings to be concatenated
    
    Returns:
        str: A single concatenated string representing all strings in the input list
    """
    # Initialize an empty string to store the final concatenated string
    concatenated = ""
    # Iterate through the list and append each string to the concatenated string
    for string in input_list:
        if string: 
            concatenated += f"{string} " 
    # Remove trailing space
    return concatenated.rstrip(' ')