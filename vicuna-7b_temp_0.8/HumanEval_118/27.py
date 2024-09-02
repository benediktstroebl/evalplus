
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
    vowels = 'aeiouAEIOU'
    word_length = len(word)
    last_consonant = word_length - 1
    closest_vowel = ''
    for i in range(last_consonant+1, word_length):
        if word[i] in vowels:
            distance = 0
            for j in range(last_consonant, i):
                if word[j] == word[i] and (j < last_consonant or word[j] != word[i-1]):
                    distance += 1
            if distance < len(word) - i - 1:
                closest_vowel = word[i]
                break
    return closest_vowel