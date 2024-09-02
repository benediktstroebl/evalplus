
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
    left_index = 0
    right_index = len(word) - 1
    closest_vowel = ""
    
    while left_index <= right_index:
        if word[left_index] == "a" or word[left_index] == "e" or word[left_index] == "i" or word[left_index] == "o" or word[left_index] == "u":
            left_index += 1
            continue
        elif word[left_index] == "b" or word[left_index] == "c" or word[left_index] == "d" or word[left_index] == "f" or word[left_index] == "g" or word[left_index] == "h" or word[left_index] == "j" or word[left_index] == "k" or word[left_index] == "l" or word[left_index] == "m" or word[left_index] == "n" or word[left_index] == "p" or word[left_index] == "q" or word[left_index] == "r" or word[left_index] == "s" or word[left_index] == "t" or word[left_index] == "x" or word[left_index] == "z":
            left_index += 1
            continue
        
        if word[right_index] == "a" or word[right_index] == "e" or word[right_index] == "i" or word[right_index] == "o" or word[right_index] == "u":
            right_index -= 1
            closest_vowel = word[left_index]
            break
        elif word[right_index] == "b" or word[right_index] == "c" or word[right_index] == "d" or word[right_index] == "f" or word[right_index] == "g" or word[right_index] == "h" or word[right_index] == "j" or word[right_index] == "k" or word[right_index] == "l"
