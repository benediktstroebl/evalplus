```python
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
    # Using dichotomous search to find the closest vowel
    n = len(word)
    index = n - 1
    while index >= 0:
        if word[index] in 'AEIOUaeiou':
            if index == 0 or word[index-1] in 'BCDFGHJKLMNPQRSTVWxyzbcdfghjklmnpqrstvw':
                return word[index]
            else:
                index -= 1
        else:
            if word[index] in 'BCDFGHJKLMNPQRSTVWxyzbcdfghjklmnpqrstvw':
                index -= 1
            else:
                return ''
        # Return if the first or last char is a vowel
        if index == -1 or index == 0:
            break
    return ''
```

The solution relies on the fact that the English alphabet contains 26 letters, and there are 9 vowels in total, making it a dichotomous search problem. The function iterates over the letters from the right using a index variable. At each step the function checks if the character at the current index is a vowel or not, if it's a vowel and if it's not the first character of the word and the character to its left is a consonant, then we return the vowel. If none of these conditions are met, we move the index backwards accordingly to investigate the next character. The same logic also applies for investigating consecutive consonant blocks. And to handle the case when the index reaches the beginning or ends of the string (where there might be a vowel), we also have breaks to handle these cases and make the function return an empty string if those situations occur.