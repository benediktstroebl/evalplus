
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
    first_vowel = False
    last_vowel = False
    consonants = []
    vowels = []

    for letter in word:
        if letter in 'aeiou':
            vowels.append(letter)
            if not first_vowel:
                first_vowel = letter
        else:
            consonants.append(letter)
        if letter in 'aeiou' and not first_vowel:
            first_vowel = letter

    last_vowel = word[-1]

    if first_vowel and last_vowel:
        if len(consonants) > 1:
            for i in range(len(consonants)):
                if i == len(consonants)-1:
                    return consonants[i-1]
    return ""
