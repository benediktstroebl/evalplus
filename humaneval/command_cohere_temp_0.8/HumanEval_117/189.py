Here's a Python script that defines a function `select_words` to solve the problem:
```python
def select_words(s, n):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    words = s.split()
    result = []
    
    for word in words:
        cnt = sum(1 for char in word if char in consonants)
        if cnt == n:
            result.append(word)
    
    return result if result else []

# Test cases
print(select_words("Mary had a little lamb", 4))     # Output: ["little"]
print(select_words("Mary had a little lamb", 3))     # Output: ["Mary", "lamb"]
print(select_words("simple white space", 2))       # Output: []
print(select_words("Hello world", 4))             # Output: ["world"]
print(select_words("Uncle sam", 3))               # Output: ["Uncle"]
```

This script assumes that the input string contains only letters and spaces, which is noted as a assumption in the problem statement. The `select_words` function splits the input string into a list of words and then iterates through each word, counting the number of consonants in the word. If this counts as n (given as input), the word is appended to the result list, and finally, this returns the list of words that contain exactly n consonants. The example usage scenarios demonstrate how the function works for different input scenarios.