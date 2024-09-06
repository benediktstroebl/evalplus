
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
    d = {}
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                continue
            if word[i] in "aeiouAEIOU" and word[j] in "aeiouAEIOU":
                if word[i] > word[j]:
                    d[word[i]] = word[i]
                elif word[j] > word[i]:
                    d[word[j]] = word[j]
                else:
                    d[word[i] + word[j]] = min(d[word[i]], d[word[j]])
    return d[min(d[key] for key in d)] if d else ""
