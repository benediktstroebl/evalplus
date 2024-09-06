```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []

    for word in word_array:
        char_array = list(word)
        char_array.sort()
        new_word = ''.join(char_array)
        new_word_array.append(new_word)

    return ' '.join(new_word_array)
```

The code splits the input string into a list of words and then iterates through each word. For each word, it creates a list of characters, sorts them alphabetically based on their ASCII values, and then joins them back to form a new word. These new words are assembled together with spaces in the original order to create the desired output. 

This approach ensures the correct ordering of characters within each word while maintaining the original word order and spacing, effectively solving the anti-shuffle task.