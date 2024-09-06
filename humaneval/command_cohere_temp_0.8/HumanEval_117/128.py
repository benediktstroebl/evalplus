```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```

Here's how the script works:
1. The `count_consonants` function counts the number of consonants in a given word. It converts the word to lowercase to ensure consistency and iterates through each character in the word. It classifies each character as a consonant or not based on the provided list of consonant characters.
2. The `select_words` function takes the input string `s` and the target number of consonants `n`. It first splits the input string into a list of words using the `split` method. Then, it initializes an empty list called `result` to store the words that match the specified criteria. It goes through each word in the list and calculates the number of consonants using the `count_consonants` function.
3. If the count of consonants in a word matches the target `n`, it appends that word to the `result` list. After processing all words, the function returns the `result` list containing the desired words.

The script accurately solves the problem and returns the required list of words containing exactly `n` consonants from the provided input string.