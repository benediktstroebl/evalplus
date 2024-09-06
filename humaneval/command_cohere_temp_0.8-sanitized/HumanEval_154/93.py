def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    # Convert the words to lower case to avoid case-sensitivity issues
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Check if word2 as is is present in word1
    if word2 in word1:
        return True
    
    # Check word2 reversed as substring in word1
    reversed_word2 = word2[::-1]
    if reversed_word2 in word1:
        return True
    
    return False