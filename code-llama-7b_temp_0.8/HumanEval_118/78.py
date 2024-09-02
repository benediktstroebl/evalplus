
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    # Solution 1: Use a stack
    # stack = []
    # for char in reversed(word):
    #     if char.isalpha():
    #         stack.append(char)
    #     else:
    #         if len(stack) > 1:
    #             return stack[-2]
    #     return ""

    # Solution 2: Use a pointer
    i = len(word) - 1
    while i >= 0:
        if word[i].isalpha():
            break
        else:
            i -= 1
    if i < 0:
        return ""
    if word[i].isalpha() and not word[i].islower():
        i -= 1
    if i < 0:
        return ""
    while i > 0:
        if word[i - 1].isalpha() and word[i - 1].islower():
            return word[i]
        i -= 1
    return ""
