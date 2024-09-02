

def same_chars(s0: str, s1: str):
    """
    Check if two words have the same characters.
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc')
    True
    >>> same_chars('abcd', 'dddddddabc')
    True
    >>> same_chars('dddddddabc', 'abcd')
    True
    >>> same_chars('eabcd', 'dddddddabc')
    False
    >>> same_chars('abcd', 'dddddddabce')
    False
    >>> same_chars('eabcdzzzz', 'dddzzzzzzzddddabc')
    False
    """
    # define a set of characters that are considered the same
    same_chars_set = set(str.lower())
    # convert the two words to a list of characters
    word0 = [c for c in s0]
    word1 = [c for c in s1]
    # remove the 'same_chars' string from the set
    same_chars_set -= 'same_chars'
    # loop through the characters of the first word
    for i in range(len(word0)):
        # check if the current character is in the set of same characters
        if word0[i] in same_chars_set:
            # if the current character is not the same as the next character,
            # then check if the current character is in the set of the second word
            if i < len(word1) and word1[i] in same_chars_set:
                # if the current character is the same as the next character of the second word,
                # then remove the same character from the set of the first word
                same_chars_set.remove(word0[i])
                # if the current character is the same as the next character of the first word,
                # then remove the same character from the set of the second word
                same_chars_set.remove(word1[i])
                # if the set of characters is not empty, then return False
                if len(same_chars_set) > 0:
                    return False
        # if the character is not in the set, then remove it from the set of the first word
        same_chars_set.remove(word0[i])
    # if the set of characters is not empty, then return True
    return True