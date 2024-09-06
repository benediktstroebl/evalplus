```python
def count_consonants(word):
    """
    Function to count the number of consonants in a word
    """
    total = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
                (char != 'y' or word[0] in 'aeiou') and char != 'w' and char != 'h':
            total += 1
    return total
    

def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants 
    in order these words appear in the string s
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result

# Test Cases
print(select_words("Mary had a little lamb", 2))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
```

This script utilizes the `count_consonants` function to tally the number of consonants in a given word. By splitting the input string into separate words and iterating through each, the script filters words that contain the specified count of consonants and stores them in the `result` list. The final output is a list of words from the input string containing exactly 'n' consonants.