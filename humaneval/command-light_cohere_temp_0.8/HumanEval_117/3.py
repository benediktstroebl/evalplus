```python
def select_words(s, n): 
    # Remove all characters except a vowel and number 
    s= [c for c in s if c.isalpha('a') or string.isdigit(c)]

    # Filter and return the words that have n consonants 
    return [word for word in s if word.count('c') == n] 

# Example usage 
print(select_words("Mary had a little lamb", 4))  # ['little']
print(select_words("Mary had a little lamb", 3))  # ['Mary', 'lamb']
print(select_words("simple white space", 2))  # []
print(select_words("Hello world", 4))  # ['world']
print(select_words("Uncle sam", 3))  # ['Uncle']
``` 
The function `select_words` takes a string `s` and an integer `n` as input. It then removes all characters except letters and numbers from the input string and returns a list of words that have exactly `n` occurrences of the consonant letter 'c'.