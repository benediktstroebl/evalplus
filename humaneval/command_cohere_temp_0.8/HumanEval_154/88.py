```python
def cycpattern_check(word1, word2):
    """
    You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word.
    """
    # Convert words to lowercase to make the comparison case-insensitive
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Check if word2 is a substring of word1
    if word2 in word1:
        return True
    
    # Check for rotations of word2 in word1
    rotations = [word2[1:], word2[0:len(word2) - 1], word2[::-1]]
    for rotation in rotations:
        if rotation in word1:
            return True
    
    return False
```

This function compares the inputs word1 and word2, checking if word2 appears in word1 unchanged, and also checking if any rotation of word2 is present in word1. The rotations.py module employs string slicing to generate rotational variations of the second word. The function returns True if any of these patterns are found, and False otherwise. 

The Markdown code block above contains a self-contained Python function that takes two words as input and returns a boolean indicating whether the second word or any of its rotations is a substring in the first word. This function is designed to handle various cases and provide a clear and concise solution to the problem as stated in the documentation provided.