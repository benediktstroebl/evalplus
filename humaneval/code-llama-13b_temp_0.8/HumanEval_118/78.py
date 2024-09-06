
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
    # consonants = 'bcdfghjklmnpqrstvwxz'
    # vowels = 'aeiou'
    # vowel_indices = [i for i in range(len(word)) if word[i].lower() in vowels]
    # consonant_indices = [i for i in range(len(word)) if word[i].lower() in consonants]
    # vowels_from_right = [index for index in reversed(vowel_indices) if index < len(word)-1 and index > max(consonant_indices)]
    # closest_vowel = ''
    # if vowels_from_right:
    #     closest_vowel = word[min(vowels_from_right)]
    # return closest_vowel
    
    vowels = "aeiou"
    consonants = 'bcdfghjklmnpqrstvwxz'
    vowels_from_right = []
    for i in range(len(word)):
        if word[len(word)-i-1].lower() in vowels:
            vowels_from_right.append(i)
    consonants_from_right = []
    for i in range(len(word)):
        if word[len(word)-i-1].lower() in consonants:
            consonants_from_right.append(i)
    vowels_from_right = [index for index in reversed(vowels_from_right) if index < len(word)-1 and index > max(consonants_from_right)]
    closest_vowel = ''
    if vowels_from_right:
        closest_vowel = word[min(vowels_from_right)]
    return closest_vowel
