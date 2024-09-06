def cycpattern_check(word1, word2):
    """
    You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word.
    """
    # Convert both words to lowercase to make the comparison case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Check if word2 as is is a substring of word1
    if word2 in word1:
        return True
    
    # Check if any rotation of word2 is a substring of word1
    rotations = [word2[i:]+word2[:i] for i in range(len(word2))]
    return any(rotations) <= word1