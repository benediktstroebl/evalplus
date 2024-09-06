
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
    if len(word)<3:
        return ''
    if word[-2]=='a' or word[-2]=='e' or word[-2]=='i' or word[-2]=='o' or word[-2]=='u':
        return word[-1]
    if word[-3]=='a' or word[-3]=='e' or word[-3]=='i' or word[-3]=='o' or word[-3]=='u':
        return word[-2]
    if word[0]=='a' or word[0]=='e' or word[0]=='i' or word[0]=='o' or word[0]=='u':
        return word[1]
    if word[1]=='a' or word[1]=='e' or word[1]=='i' or word[1]=='o' or word[1]=='u':
        return word[2]

    return ''





















