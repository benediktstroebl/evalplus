```python
def cycpattern_check(word1, word2):
    """
    You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word.
    """
    if len(word1) < len(word2):
        return False
    if word2 in word1:
        return True
    # Iterate over possible rotations of word2 and check if any of them are in word1
    for i in range(len(word2)):
        rotate = word2[i:] + word2[:i]
        if rotate in word1:
            return True
    return False
```

This function checks if the second word is a substring of the first word, and also checks if any rotation of the second word is a substring of the first word. It returns 'True' if any of these conditions are met, and 'False' otherwise. 

You can use it by calling the function with two input words, as shown in the comments in the code block above. Let me know if you would like me to explain anything in this script further.