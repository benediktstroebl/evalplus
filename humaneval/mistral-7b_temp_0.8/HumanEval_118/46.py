
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

    # your code here
    #  if len(word) < 2:
    #      return ""
    #  vowel_list = ['a', 'e', 'i', 'o', 'u']
    #  if len(word) == 2:
    #      if word[0].lower() not in vowel_list and word[1].lower() not in vowel_list:
    #          return ""
    #      else:
    #          return word[0] if word[0].lower() not in vowel_list else word[1]
    #  if word[0].lower() not in vowel_list and word[-1].lower() not in vowel_list:
    #      return word[0]
    #  if word[-1].lower() not in vowel_list:
    #      return word[-1]
    #  return ""

    vowels = 'aeiou'
    for i in range(1, len(word) - 1):
        if word[i].lower() not in vowels:
