
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
    
    def get_distance(ch1, ch2):
        if ch1 == "a" and ch2 == "e": return 1
        if ch1 == "e" and ch2 == "a": return 1
        if ch1 == "i" and ch2 == "o": return 1
        if ch1 == "o" and ch2 == "i": return 1
        if ch1 == "u" and ch2 == "y": return 1
        if ch1 == "y" and ch2 == "u": return 1
        
    vowels = "aeiouy"
    char_idx = len(word)
    
    while char_idx > 0:
        prev_char = word[char_idx-1]
        curr_char = word[char_idx]
        if curr_char not in vowels:
            char_idx -= 1
        else:
            break
    
    if char_idx == 0: return ""
    
    vowel_distance = get_distance(word[char_idx-1], word[char_idx])
    for i in range(char_idx, len(word)):
        curr_char = word[i]
        curr_next_char = word[i+1] if i+1 < len(word) else None
        if curr_char not in vowels:
            vowel_distance = min(vowel_distance, get_distance(prev_char, curr_char) + 1)
        if curr_next_char:
            vowel_distance = min(vowel_distance, get_distance(prev_char, curr_next_char) + 1)
        prev_char = curr_char
    
    return word[char_idx-1-vowel_distance: char_idx-1]

assert get_closest_vowel("yogurt") == "u"
assert get_closest_vowel("FULL") == "U"
assert get_closest_vowel("quick") == ""
assert get_closest_vowel("ab") == ""
assert