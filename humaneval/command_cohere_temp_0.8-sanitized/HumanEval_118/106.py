def get_closest_vowel(word):
    """
    Find the closest vowel to the right of the word, if there is one between two consonants.
    """
    vowels = 'AEIOUaeiou'  
    ll = len(word) 
    k = len(word) - 1 
    while k >= 0 and word[k] in 'QWERTYUIOPASDFGHJKLZXCVBNM' : 
        if word[k] in vowels : 
            if word[k-1] in 'QWERTYUIOPASDFGHJKLZXCVBNM' : 
                return word[k] 
        k -= 1 
    return ''