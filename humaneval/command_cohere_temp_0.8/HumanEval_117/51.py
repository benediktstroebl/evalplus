```python
def count_consonants(word):
    count = 0
    for char in word:
        if char != 'a' and char != 'e' and char != 'i' and char != 'o' and char != 'u' and \
           char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U' and \
           char != 'y' and char != 'Y':
            count += 1
    return count

def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        if count_consonants(word) == n:
            result.append(word)
    return result if result else ["None"]

# Example usage
print(select_words("Mary had a little lamb", 3))
print(select_words("simple white space", 2))
print(select_words("Hello world", 4))
print(select_words("Uncle sam", 3))
```

This script divides the string into a list of words space by space, then iterates over each word, counting the number of consonants in each word, and finally adds to the result list those words that have exactly the desired number of consonants. In the case of an empty string, it returns a list with the word "None".