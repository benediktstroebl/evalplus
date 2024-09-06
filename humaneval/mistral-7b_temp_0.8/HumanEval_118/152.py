
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
    # Your code here
    vowels = 'aeiou'
    new_word = ''.join(list(filter(lambda x: x not in vowels, word)))
    vowels_and_word = word.split(new_word)
    if vowels_and_word[0] == '' and vowels_and_word[1] == '':
        return ''
    elif vowels_and_word[0] != '' and vowels_and_word[1] == '':
        return ''
    else:
        return vowels_and_word[1]
