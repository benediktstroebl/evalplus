

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    # Use a regular expression to split the string into words
    words = re.split(r'\w', string)
    
    # Use a dictionary to store the first character of each word
    char_map = {}
    
    # Loop through the words and flip the case of each character
    for word in words:
        for i in range(len(word)):
            if word[i] in char_map:
                char_map[word[i]] = char_map.pop(word[i])
            else:
                char_map[word[i]] = word[i].upper()
    
    # Join the characters in the dictionary back into a string
    result = ''.join(char_map)
    
    return result
