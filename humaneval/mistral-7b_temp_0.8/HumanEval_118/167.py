
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
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    consonant_list = []
    vowel_list = []
    word_list = []
    for i in range(len(word)):
        word_list.append(word[i])
    for j in range(len(word_list)):
        if word_list[j].lower() in consonant:
            consonant_list.append(word_list[j])
        if word_list[j].lower() in vowel:
            vowel_list.append(word_list[j])
    if consonant_list.count('') > 0:
        consonant_list.remove('')
    if vowel_list.count('')
