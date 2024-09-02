
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

    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_position = []
    word = list(word)
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_position.append(i)

    if vowel_position == []:
        return ""
    else:
        if vowel_position[0] == 0:
            return vowels[vowel_position[1]]
        if vowel_position[-1] == len(word)-1:
            return vowels[vowel_position[-2]]
        else:
            return vowels[vowel_position[0]]
