
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
    n = len(word)
    vowels = 'aeiouAEIOU'
    for i in range(n-1, -1, -1):
        for j in range(i, n):
            if word[j] in vowels:
                if word[i] == 'a':
                    if word[j] == 'a':
                        if word[j+1] in vowels:
                            return word[j+1]
                        elif word[j+2] in vowels:
                            return word[j+2]
                elif word[j] == 'e':
                    if word[j+1] in vowels:
                        return word[j+1]
                    elif word[j+2] in vowels:
                        return word[j+2]
                elif word[j] == 'i':
                    if word[j+1] in vowels:
                        return word[j+1]
                    elif word[j+2] in vowels:
                        return word[j+2]
                elif word[j] == 'u':
                    if word[j+1] in vowels:
                        return word[j+1]
                    elif word[j+2] in vowels:
                        return word[j+2]
                elif word[j] == 'o':
                    if word[j+1] in vowels:
                        return word[j+1]
                    elif word[j+2] in vowels:
                        return word[j+2]
    return ''