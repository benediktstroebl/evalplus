
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
    #my solution
    # print('the string is', word)
    # if len(word) < 3:
    #     return ''
    # else:
    #     for i in range(len(word)-1, 1, -1):
    #         if word[i].isalpha() and word[i-1].isalpha() and word[i+1].isalpha() and (word[i].isupper() == word[i-1].isupper() == word[i+1].isupper()):
    #             if word[i].lower() in 'aeiou':
    #                 return word[i]


    #leetcode solution
    vowels = 'aeiou'
    low = 'AEIOU'
    for i in range(len(word)-1, -1, -1):
        if word[i].isalpha() and word[i-1].isalpha() and word[i+1].isalpha():
            if word[i].islower() and word[i-1].isupper() != word[i+1].isupper():
                return word[i]
            if word[i].isupper() and word[i-1].islower() != word[i+1].islower():
                return word[i]
            if word[i].islower() and word[i-1].islower() != word[i+1].islower():
                return word[i]
            if word[i].isupper() and word[i-1].isupper() != word[i+1].isupper():
                return word[i]
    return ''
