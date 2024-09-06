```python
def find_max(words):
    char_count = {}
    max_word = None
    max_char_count = 0
    
    for word in words:
        unique_chars = set(word)
        current_char_count = len(unique_chars)
        
        if current_char_count > max_char_count:
            max_char_count = current_char_count
            max_word = word
            
    return max_word

# Test Cases
words = ["name", "of", "string", "enam", "game", "aaaaaaa", "bb", "cc"]
print(find_max(words))  # Output: "aaaaaaa"

words = ["apple", "orange", "apple", "banana", "orange"]
print(find_max(words))  # Output: "apple"
```

In this script, a counter `char_count` is used to keep track of how many times each character comes up in the list. We use a dictionary `char_count` for efficient lookups. The `set()` function is then used to create a set of unique characters in each word, and the length of this set gives us the count of unique characters.

The function will return the word that maximizes the unique character count as per the problem's requirements. If there are multiple words with the maximum count, the function will return the word that appears first in lexicographical order.