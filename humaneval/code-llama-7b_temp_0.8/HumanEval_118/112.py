
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
    # Rough plan: find the rightmost consonant
    #   find all vowels to the right
    #   find the closest vowel
    #   if the closest vowel is to the left of the rightmost consonant,
    #     find all vowels to the left
    #     find the closest vowel
    #     return the closest of the two closest vowels
    #   else return the only closest vowel
    #   (or empty string if there are no vowels to the right or to the left of the
    #     rightmost consonant)
    
    def find_rightmost_consonant(word):
        i = len(word) - 1
        while i >= 0:
            if word[i] not in "aeiouAEIOU":
                return i
            i -= 1
        return -1
    
    def find_all_vowels(word, start_index, end_index):
        return [letter for letter in word[start_index:end_index] if letter in "aeiouAEIOU"]
    
    def find_closest_vowel(word, rightmost_consonant, vowels):
        for i in range(len(vowels) - 1, -1, -1):
            if vowels[i] > word[rightmost_consonant]:
                return vowels[i]
        return ""
    
    def find_all_vowels_to_right(word, rightmost_consonant):
        return find_all_vowels(word, rightmost_consonant, len(word))
    
    def find_all_vowels_to_left(word, rightmost_consonant):
        return find_all_vowels(word, 0, rightmost_consonant)
    
    def find_closest_vowel_to_both_sides(word, rightmost_consonant, vowels_to_right, vowels_to_left):
        if len(vowels_to_left) == 0 and len(vowels_to_right) == 0:
           
