```python
def cycpattern_check(word1, word2):
    """
    You are given 2 words. Return True if the second word or any of its rotations is a substring in the first word.
    """
    if word1 == word2:
        return True
    if len(word1) != len(word2):
        return False
    letters_map = {letter: word2.count(letter) for letter in set(word2)}
    return any(letter in letters_map and letters_map[letter] > 1 for letter in word1)
```

The function uses a letters map to count the occurrences of each letter in the second word. If any letter appears more than once in the second word (i.e., it has a rotational equivalence), it checks if that letter exists in the first word. 

It returns True if any of these letters in the first word match the rotational equivalences in the second word.

To ensure efficiency, the solution does not use any wildcard searches or regex, making it linearly scalable for word lengths.