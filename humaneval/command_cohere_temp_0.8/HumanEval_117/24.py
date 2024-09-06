```python
def count_consonants(word):
    """
    Counts the number of consonants in a word
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    """
    Returns a list of words from string s that contain exactly n consonants
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```

Here's an example of how you can use the function to solve the problem statement:
```python
input_string = "Mary had a little lamb"
n = 3

selected_words = select_words(input_string, n)
print(selected_words)
```

This will output:
```
['Mary', 'lamb']
```

The script provides two functions:
- `count_consonants(word)`: This function takes a word as input, converts it to lowercase, and then loops through each character in the word. It checks if each character is a consonant and increments a counter if it is. After checking all characters, the function returns the total count of consonants in the word.
- `select_words(s, n)`: This function takes a string `s` and an integer `n` as input. It first splits the input string into a list of words, then iterates through each word. For each word, it calls `count_consonants()` to count the number of consonants in the word. If this count matches the specified `n`, the word is added to a list called `result`. Finally, the function returns this list of selected words.

The example usage demonstrates how to call `select_words()` with an input string and a desired number of consonants. The function selects the words from the string that meet this requirement and stores them in the `selected_words` list. The final output prints these selected words.