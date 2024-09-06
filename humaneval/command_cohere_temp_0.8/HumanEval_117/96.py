```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    A consonant is a letter that is not a vowel (case-insensitive).
    """
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_lowercase = 'aeiouAEIOU'
    vowel_uppercase = 'AEIOU'
    return sum(1 for char in word if char.lower() not in vowel_lowercase and char not in vowel_uppercase)

def select_words(s, n):
    """
    Given a string s and an integer n, return a list of all words from string s that contain exactly n consonants, in order these words appear in the string s.
    A word contains a vowel if it contains at least one vowel character, and contains a consonant if it contains at least one consonant character.
    If the string s is empty then the function should return an empty list.
    """
    if not s:
        return []

    words = s.split(' ')
    result = []

    for word in words:
        word_consonants = count_consonants(word)
        if word_consonants == n:
            result.append(word)

    return result
```

The `count_consonants` function is a utility function that calculates the number of consonants in a given word, which is used by the `select_words` function to filter and retrieve the words that contain exactly the desired number of consonants. This solution passes the test cases provided in the prompt, including edge cases. The approach is simple and straightfoward. It iterates through the words in the string and uses the `count_consonants` function to count the number of consonants in each word. If the count matches the desired number, the word is added to the result list.  The final result is a list of words that contain exactly `n` consonants.  The code is efficient and can easily scale to handle longer strings and larger values of `n`.  It also handles potential edge cases, such as empty input strings or cases where no words meet the criteria. 

Here is how you can use it:
```python
>>> select_words("Mary had a little lamb", 3)
['Mary', 'lamb']

>>> select_words("simple white space", 2)
[]

>>> select_words("Hello world", 4)
['world']

>>> select_words("Uncle sam", 3)
['Uncle']
``` 
This solution is reusable and can be applied to various scenarios involving counting consonants or vowels in words or tokens of a string.