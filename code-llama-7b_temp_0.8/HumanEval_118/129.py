
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
    # First attempt:
    # for i in range(len(word)-1, 0, -1):
    #     if word[i].isalpha():
    #         if word[i].lower() in 'aeiou':
    #             if word[i] == 'o' or word[i] == 'u':
    #                 return word[i]
    #             elif word[i-1] in 'aeiou':
    #                 return word[i]
    #             else:
    #                 return word[i-1]
    # return ''

    # Second attempt:
    # for i in range(len(word)-1, 0, -1):
    #     if word[i].isalpha():
    #         if word[i].lower() in 'aeiou':
    #             if word[i-1] in 'aeiou':
    #                 return word[i]
    #             elif word[i-1] not in 'aeiou' and word[i] in 'aeiou':
    #                 return word[i]
    # return ''

    # Third attempt:
    # for i in range(len(word)-1, 0, -1):
    #     if word[i].isalpha():
    #         if word[i].lower() in 'aeiou':
    #             if word[i-1] not in 'aeiou' and word[i] in 'aeiou':
    #                 return word[i]
    #             elif word[i-1] not in 'aeiou' and word[i] not in 'aeiou':
    #                 return word[i-1]
    #             elif word[i-1] in 'aeiou' and word[i] not in 'aeiou':
    #                 return word[i]
    #             elif word[i-1] in 'aeiou' and word[i] in 'aeiou':
    #                 return word[i]
    # return ''

    # Fourth attempt:
    # for i in range(len(word)-1, 0, -1):
    #     if word[i].isalpha
