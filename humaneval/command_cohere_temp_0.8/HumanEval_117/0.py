```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            total += 1
    return total

def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants, 
    in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    """
    words = s.split(' ')
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)

    return result
```

The approach used by the function `select_words` is to first split the input string into words and then use the helper function `count_consonants` to count the number of consonants in each word. Then for each word, if the count of consonants is equal to the given `n`, it gets appended to the result list. Lastly, the function returns the list containing the words that meet the criteria. 

The consonant counting function `count_consonants` is utilizing a simple loop to iterate over each character in the word and checks if each character is a consonant, incrementing a total count if it is.