Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string that contain exactly n consonants:
```python
def select_words(s, n):
    words = s.split(' ')
    result = []
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    
    for word in words:
        num_consonants = sum(1 for char in word if char in consonants)
        if num_consonants == n:
            result.append(word)
    
    return result if result else ['None']

# Example Usage
input_str = "Mary had a little lamb"
n = 3
print(f'Function output: {select_words(input_str, n)}')
```

This script assumes that the input string contains only letters and spaces, which is noted as a assumption in the problem statement. The script also assumes that the number of consonants considered is a natural number value. The script splits the input string into individual words and then counts the number of consonants in each word. If the count matches the specified number n, the word is added to a list result. Finally, the script returns the list of words that match the criteria. 

Note that the string "None" is returned in the code if there are no words in the input string. This is used for blank strings and is appended to the list to indicate no words were found.