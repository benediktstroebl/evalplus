
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
    start = 0
    end = len(word) - 1
    closest_index = -1
    while start <= end:
        if word[start] == word[end] and word[start] == "c" or word[start] == "s" or word[start] == "t" or word[start] == "p" or word[start] == "h":
            end -= 1
        else:
            if word[start] == "e" or word[start] == "i" or word[start] == "u" or word[start] == "o":
                closest_index = start
            start += 1
    return closest_index == -1 and "" or word[closest_index]

test = [get_closest_vowel("yogurt"), get_closest_vowel("FULL"), get_closest_vowel("quick"), get_closest_vowel("ab"), get_closest_vowel("water"), get_closest_vowel("kite"), get_closest_vowel("math"), get_closest_vowel("computer")]

for test_case in test:
    print(test_case)

print("Number of test cases:", len(test))
