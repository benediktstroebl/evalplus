Here's a Python script that contains a function called `select_words` which solves the problem you've described:
```python
def select_words(s, n):
    """
    Find words in a string that contain a certain number of consonants.
    """
    def count_consonants(word):
        c = 0
        for letter in word:
            if letter in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
                c += 1
        return c
    
    words = [word.strip() for word in s.split(' ') if word.strip()]
    result = [word for word in words if count_consonants(word) == n]
    return result

# Test Cases
assert select_words("Mary had a little lamb", 4) == ["little"]
assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
assert select_words("simple white space", 2) == []
assert select_words("Hello world", 4) == ["world"]
assert select_words("Uncle sam", 3) == ["Uncle"]
```

This script uses a nested approach where the `count_consonants` function counts the consonants received, and the `result` list is populated by filtering words based on this count. It also properly handles empty strings and cases where the number of consonants requested is greater than or equal to the total number of consonants in the entire input string.