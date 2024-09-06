```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_characters = set(word)
        char_count[word] = len(unique_characters)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_count = max(char_count.values())
    return char_count[lexicographically_first] if char_count[lexicographically_first] == max_count else lexicographically_first
```

The code works by first counting the number of unique characters in each word. Then, it identifies the word with the highest count of unique characters, considering the lexicographical order when there's a tie. 

To better understand the code, let's break it down step by step:
1. **Dict for Character Count**: Sets up a dictionary, `char_count`, where each element is a word in the input list and its corresponding value is the count of unique characters. 
2. **Identify Lexicographically First Word with Maximum Unique Characters**: By iterating through the input list, the code simultaneously tracks the word with the highest count of unique characters and the word that appears first in the lexicographical order. 
3. **Handling Tie**: In case multiple words have the same highest count of unique characters, the code returns the word that appeared first in the input list. 

The script optimizes the process by tracking both unique character counts and lexicographical order, reducing the complexity to O(n), where 'n' is the length of the input list.