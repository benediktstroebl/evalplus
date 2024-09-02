
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
    last_caracter = word[-1]
    current_caracter = word[-2]
    if last_caracter in 'aeiou': return word[-1]
    if current_caracter in 'aeiou': return word[-2]
    
    vowels = 'aeiou'
    smallest_score = len(word)
    score = 0
    for char in word[::-1]:
        if char in vowels:
            score += 1
            if score == 3: break
        score -= 1
    if score < smallest_score:
        return word[::-1][score:]
    return ''

