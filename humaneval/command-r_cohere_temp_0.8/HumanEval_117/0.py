```python
def select_words(s, n):
    """Returns a list of words with exactly n consonants.

    Args:
        s (str): Input string containing words separated by spaces.
        n (int): Number of consonants to filter by.

    Returns:
        list: Words with exactly n consonants, in order of appearance.

    Examples:
        >>> select_words("Mary had a little lamb", 4)
        ['little']

        >>> select_words("Mary had a little lamb", 3)
        ['Mary', 'lamb']

        >>> select_words("simple white space", 2)
        []

        >>> select_words("Hello world", 4)
        ['world']

        >>> select_words("Uncle sam", 3)
        ['Uncle']
    """
    words = s.split()
    result = []
    
    for word in words:
        consonants = 0
        for char in word:
            if char.isalpha():
                consonants += 1
        if consonants == n:
            result.append(word)
    
    return result
```