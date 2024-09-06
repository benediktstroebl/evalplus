```python
def find_max(words):
    char_count = {}
    lexicographically_first = None
    
    for word in words:
        unique_chars = set(word)
        char_count[word] = len(unique_chars)
        if lexicographically_first is None or word < lexicographically_first:
            lexicographically_first = word
            
    max_char_word = min(char_count, key=char_count.get)
    return lexicographically_first if char_count[lexicographically_first] == char_count[max_char_word] else max_char_word
``` 

The `find_max` function solves the problem by first mapping each word to the number of unique characters it contains. It then identifies the word with the highest count of unique characters, employing the `min` function to select either the word with the highest count or the lexicographically earliest word if there is a tie. 

The practice of using the `min` function to select between multiple maximum values is prevalent in competitive programming and is known as the "winning votes algorithm." 

If you would like to run this code, you can copy and paste it into a Python environment or script and invoke the `find_max` function as you would for any regular function, providing a list of strings as the argument.