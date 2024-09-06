
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

    
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l','m', 'n', 'p', 'q', 'r','s', 't', 'v', 'w', 'x', 'y', 'z']
    
    consonants_indexes = []
    vowels_indexes = []
    
    for i in range(len(word) - 1):
        if word[i] in consonants:
            consonants_indexes.append(i)
        if word[i] in vowels:
            vowels_indexes.append(i)
    
    if len(consonants_indexes) == 1:
        return word[consonants_indexes[0]]
    
    if len(consonants_indexes) == 2:
        return word[min(consonants_indexes)]
    
    for vowel_index in vowels_indexes:
        
