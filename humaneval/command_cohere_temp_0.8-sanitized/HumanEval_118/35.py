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
    # Using tuple to sort and count the frequency
    counter = dict()
    vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
    word = word.lower()
    word = word[1:-1] if len(word) > 2 else word
    for letter in word:
        if letter in vowel:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
    # Search the max frequency value
    largest_freq = max(counter.values())
    # Search the vowel which max frequency
    for k, v in counter.items():
        if v == largest_freq:
            return k
    return ""