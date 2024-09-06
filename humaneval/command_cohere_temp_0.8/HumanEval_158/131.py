```python
def find_max(words):
    char_count = {}
    lexic_front = []
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if char_count[word] == max(char_count.values()):
            lexic_front.append(word)
            
    return min(lexic_front)
```

The Python script defines a function `find_max` that solves the problem statement using the following approach:
1. Initialize an empty dictionary, `char_count`, to store the unique characters in each word, and an empty list, `lexic_front`, to store the words that maximize the unique characters. 
 2. Iterate through each word in the input list. For each word:
    - Compute its unique characters by converting it to a set.
    - Update the dictionary `char_count` with the count of unique characters.
    - If the count is equal to the maximum count among existing values, append the word to the `lexic_front` list. 
 3. Finally, return the first element in the `lexic_front` list, which represents the word with the most unique characters, considering lexicographical order. 

This approach efficiently solves the problem using dictionary and set operations, and ensures the correct word is selected in case of a tie in the maximum number of unique characters.