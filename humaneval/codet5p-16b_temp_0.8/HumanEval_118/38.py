
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

    import re

    word_list = re.findall('[a-z]+', word)

    for i in range(len(word_list)):
        if 'b' in word_list[i] or 'c' in word_list[i] or 'd' in word_list[i] or 'f' in word_list[i] or 'g' in word_list[i] or 'h' in word_list[i] or 'j' in word_list[i] or 'k' in word_list[i] or 'l' in word_list[i] or'm' in word_list[i] or 'n' in word_list[i] or 'p' in word_list[i] or 'q' in word_list[i] or 'r' in word_list[i] or's' in word_list[i] or 't' in word_list[i] or 'v' in word_list[i] or 'w' in word_list[i] or 'x' in word_list[i] or 'y' in word_list[
