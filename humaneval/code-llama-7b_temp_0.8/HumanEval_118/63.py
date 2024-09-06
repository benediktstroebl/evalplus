
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
    # Rules
    # - vowels in the beginning and ending does not count.
    # - find the closest vowel that stands between two consonants
    # - return empty string if you didn't find any vowel meets the above condition.
    # - You may assume that the given string contains English letter only.

    # 1st solution:
    # reverse string and then use the same code to find the closest consonants
    # O(n) time | O(n) space - where n is the length of the input string
    # reverse_word = word[::-1]
    # closest_consonants = get_closest_consonants(reverse_word)
    # if closest_consonants:
    #     return closest_consonants[0]
    # else:
    #     return ''

    # 2nd solution:
    # two pointers
    # O(n) time | O(1) space
    # reverse string and then use the same code to find the closest consonants
    # O(n) time | O(n) space - where n is the length of the input string
    closest_vowel = ''
    left = 0
    right = len(word) - 1

    while right > left:
        if word[left] in 'aeiou':
            left += 1
        elif word[right] in 'aeiou':
            right -= 1
        else:
            left += 1
            right -= 1
            if word[left] in 'aeiou' and word[right] in 'aeiou':
                closest_vowel = word[left] if word[left] == word[left - 1] else word[right]
                break

    return closest_vowel
