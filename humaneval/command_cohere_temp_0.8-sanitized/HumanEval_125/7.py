import re
def split_words(txt):
    """
    Split the input text into words, handling various types of whitespace.
    
    Args:
        txt (str): The input text to split.

    Returns:
        list: List of words split from the input text.
    """
    # Handle various types of whitespace and split the text into words
    word_tokens = re.split(r'\s*,\s*', txt)
    
    if not word_tokens:
        # If no words are found, return an empty list
        return []
    
    # If all words consist of only lowercase letters with odd alphabetical order, return the count of words
    words = [word.lower() for word in word_tokens]
    if all(word in 'abcdefghijklmnopqrstuvwxyz' for word in words):
        return len(word_tokens)
    
    return word_tokens