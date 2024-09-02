
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
    # vowel_list = ['a', 'e', 'i', 'o', 'u']
    # vowel_index = []
    # for i in range(len(word)):
    #     if word[i] in vowel_list:
    #         vowel_index.append(i)

    # if len(vowel_index) == 1:
    #     return ''

    # else:
    #     for i in range(vowel_index[1:]):
    #         vowel_list = ['a', 'e', 'i', 'o', 'u']
    #         print(vowel_list[i])
    #         if word[vowel_index[i]] in vowel_list:
    #             return word[vowel_index[i]]
    #     return ''

    # Your code here
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    vowel_index = []
    for i in range(len(word)):
        if word[i] in vowel_list:
            vowel_index.append(i)

    if len(vowel_index) == 1:
        return ''

    else:
        for i in range(vowel_index[1:]):
            if word[vowel_index[i]] in vowel_list:
                return word[vowel_index[i]]
        return ''

