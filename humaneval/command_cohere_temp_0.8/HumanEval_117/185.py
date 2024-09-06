Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string s that contain exactly n consonants, in the order that they appear in the string:
```python
def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split(' ')
    result = []

    for word in words:
        cnt = sum(1 for char in word if char in consonants)
        if cnt == n:
            result.append(word)

    return result if result else []

# Test cases
print(select_words("Mary had a little lamb", 4))  # Output: ['little']
print(select_words("Mary had a little lamb", 3))  # Output: ['Mary', 'lamb']
print(select_words("simple white space", 2))  # Output: []
print(select_words("Hello world", 4))  # Output: ['world']
print(select_words("Uncle sam", 3))  # Output: ['Uncle']
```

This script first creates a list of all the words in the input string s by splitting it using space as a delimiter. Then, it counts the number of consonants in each word using a generator expression and adds it to the total if it matches the required count n. Finally, it returns a list of words that match the criteria. Note that this algorithm is case-insensitive, so it will work for both uppercase and lowercase letters.