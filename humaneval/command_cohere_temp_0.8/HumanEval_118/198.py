```python
def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    res = ''
    for i in range(len(word)-1):
        if word[i] in vowel and word[i+1] in consonants and (res == '' or abs(vowel.find(res) - word[i] ) > abs(vowel.find(word[i]) - word[i+1])):
            res = word[i]
    return res
```

The script works by first creating two strings, `consonants` and `vowel`, which contain all English consonants and vowels, respectively. It then loops over the word with a step of 1 (excluding the last character), and checks if the current character is a vowel and the next character is a consonant. If these conditions are met, it checks if the current vowel is closer to the beginning of the word than the previous chosen vowel. If so, it updates the `res` variable to store the current vowel. The loop continues until the end of the word is reached, at which point the `res` variable is checked and returned if it contains a non-empty string.

This algorithm has a time complexity of O(n), where n is the length of the input word, as it requires iterating over the word once, with an additional check for each character to determine if it is a vowel or a consonant. 

It assumes that the given word contains only English letters, which may be a restrictive assumption for some users. However, if the input contains other characters, the function may still work, but the behavior is less predictable and reliable.