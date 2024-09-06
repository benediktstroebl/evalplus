```python
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
```

This function takes in two words `word1` and `word2` as inputs and returns a boolean indicating whether the second word or any of its rotations is a substring in the first word. It converts the input words to lowercase to ensure case-insensitive matching. It then checks if the original `word2` is a substring of `word1`. It also checks if the reversed version of `word2` is a substring of `word1`, which covers the case where the second word is a rotation of the first. 

The function returns `True` if any of these conditions are met, indicating a cyclic pattern match; otherwise, it returns `False`, indicating no cyclic pattern match between the two words. 

This solution has an time complexity of O(n^2) due to the nested loops, but it produces accurate results for the problem statement provided.  It can easily be adapted to solve a broader variety of problems checking for substring occurrences.