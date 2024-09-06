
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
    # use a dictionary to store vowel frequency
    vowels = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
    vowel_freq = {}
    for letter in word:
        if letter in vowels:
            vowel_freq[letter] = vowels.count(letter)
    vowels = sorted(list(vowel_freq.items()), key=lambda x: x[1], reverse=True)
    start = 0
    end = 0
    while end < len(word) - 1:
        if word[start] == 'c' and word[end] == 'c':
            # ignore when the word starts or ends with "cc"
            start = 1
        elif word[start] == 's' and word[end] == 's':
            # ignore when the word starts or ends with "ss"
            start = 2
        elif word[start] == 'l' and word[end] == 'l':
            # ignore when the word starts or ends with "ll"
            start = 2
        elif word[start] in ['h', 'w'] and word[end] in ['h', 'w']:
            # ignore silent letters
            start = 2
        else:
            break
        start += 1
    start = min(len(word)-1, start)
    end = len(word)
    for i in range(start, end+1):
        if word[i] == vowels[0] and word[i+1] == vowels[-1]:
            return word[i]
    return ""