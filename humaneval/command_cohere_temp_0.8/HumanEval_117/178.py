```python
def count_consonants(word):
    """
    This function counts the number of consonants in a given word.
    """
    word = word.lower()
    total = 0
    for c in word:
        if c in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total
    
def select_words(s, n):
    """
    This function selects words from a string that contain exactly n consonants.
    """
    words = s.split()
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)
    return result
```
The `count_consonants` function is used to count the number of consonants in a given word. The `select_words` function splits the input string into words, loops through each word, and checks if the consonant count matches the required number `n`. Words that meet this condition are added to the result list, which is returned finally.

The markdown code block for the solution can be copied and pasted into a Markdown or GitHub wiki page to display the solution in a formatted code block.  This solution assumes that the input string only contains letters and spaces, and the response will be a list of words that contain exactly n consonants.  This would be the expected behavior for the given problem statement, as the first example demonstrates.