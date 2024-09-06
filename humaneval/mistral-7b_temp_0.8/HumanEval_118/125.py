
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
    word = word.lower()
    word_list = list(word)
    final = []
    for i in range(len(word_list)-1):
        if word_list[i] == 'a' or word_list[i] == 'e' or word_list[i] == 'i' or word_list[i] == 'o' or word_list[i] == 'u':
            final.append(word_list[i])
            break
    else:
        final.append("")
    for i in range(len(word_list)-1):
        if word_list[i] == 'a' or word_list[i] == 'e' or word_list[i] == 'i' or word_list[i] == 'o' or word_list[i] == 'u':
            final.append(word_list[i])
            break
    else:
        final.append("")
    for i in range(len(word_list)-1):
        if word_list[i] == 'a' or word_list[i] == 'e
