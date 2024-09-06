```python
def count_consonants(word):
    """Count consonants in a word"""
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    """Returns a list of words from string s that contain exactly n consonants"""
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is used to count the number of consonants in a given word, and the `select_words` uses this to filter out words that contain exactly *n* consonants. 

You can test this script by calling the `select_words` function with different input values to see the resulting lists of words. 
```python
select_words("Mary had a little lamb", 4)
```
This will output: `["little"]`. 

If you run this code in a Python environment that supports Markdown, you can copy the code blocks and run them directly in order to test out the code and see the results.