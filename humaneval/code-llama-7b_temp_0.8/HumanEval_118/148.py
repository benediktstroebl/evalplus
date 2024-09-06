
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
    #  2 different ways of getting it
    #   1. just checking all possible ways to find a vowel that is after two consecutive consonants
    #   (11 steps)
    # def get_closest_vowel(word):
    #     i = len(word) - 3
    #     while i >= 0:
    #         if word[i].isupper():
    #             if word[i+1].isupper():
    #                 if word[i+2].islower():
    #                     return word[i+2]
    #         i -= 1
    #     return ''
    #   2. using the string.find(sub, start, end) (16 steps)
    # def get_closest_vowel(word):
    #     # index of the last vowel from the right
    #     i = len(word) - 1
    #     while i >= 0:
    #         if word[i].isupper():
    #             # index of the first consonant from the left
    #             j = i - 1
    #             while j >= 0:
    #                 if word[j].isupper():
    #                     return word[i]
    #                 j -= 1
    #         i -= 1
    #     return ''
    # 3. using regex (8 steps)
    # import re
    # def get_closest_vowel(word):
    #     matches = re.findall(r"(?=([a-zA-Z])[A-Z][a-z](?=[a-zA-Z]))", word)
    #     if len(matches) > 0:
    #         return matches[0]
    #     return ''

    # 4. using the string.find(sub, start, end) (9 steps)
    # def get_closest_vowel(word):
    #     # index of the last vowel from the right
    #     i = len(word) - 1
    #     while i >= 0:
    #         if word[i].isupper():
    #             # index of the first consonant from the left
