```python
def count_consonants(word):
    """
    Helper function to count the number of consonants in a word.
    """
    word = word.lower()
    total = 0
    for char in word:
        if char in 'bcdfghjklmnpqrstvwxyz':
            total += 1
    return total

def select_words(s, n):
    """
    Returns a list of all words from string s that contain exactly n consonants.
    """
    if not s:
        return []

    words = s.split()
    result = []

    for word in words:
        consonant_count = count_consonants(word)
        if consonant_count == n:
            result.append(word)

    return result
```

The approach employed here is straightforward. We first split the input string into individual words and then proceed to gauge the quantity of consonants in each word, taking into account both capital and lowercase variations of consonants. Should the count match the specified number, the word is added to the resultant array.

Here's how you can test these functions:
```python
def test_count_consonants():
    assert count_consonants("hello world") == 3
    assert count_consonants("uncle sam") == 3
    assert count_consonants("bcdf") == 4
    assert count_consonants("aeiou") == 0

def test_select_words():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("bcdfgHJK", 1) == []
```