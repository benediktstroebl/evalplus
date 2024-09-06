

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # We are going to iterate through the string and count the distinct characters
    # and we will use a dictionary to store the counts of characters
    character_counts = {}
    
    # Iterate through the string
    for char in string:
        # Get the unicode value of the character
        char_unicode = char.decode()
        
        # Check if the character is in the dictionary, if not, increment the count
        if char_unicode not in character_counts:
            character_counts[char_unicode] = 1
        else:
            character_counts[char_unicode] += 1
    
    # Return the count of distinct characters
    return len(character_counts)