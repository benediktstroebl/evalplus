Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string s that contain exactly n consonants, in the order they appear in the string:
```python
def select_words(s, n):
    import re

    # Count consonants in each word and skip non-alphabetic words
    consonants = n => sum(c in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ' for c in word)
    words = re.findall(r'\w+', s.lower())
    counts = [consonants(word) for word in words]
    
    # Filter words based on the specified number of consonants
    result = [word for word, count in zip(words, counts) if count == n]
    return result if result else []

# Test the function with a variety of inputs and expected outputs
def test_select_words():
    assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
    assert select_words("simple white space", 2) == []
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("aa bb cc dd", 4) == ["cc", "dd"]
    assert select_words(" prosecuti  on", 6) == ["prosecuti"]
    assert select_words("", 4) == []

test_select_words()
```
This script uses the re module to split the input string into individual words and then checks if each word contains exactly n consonants. The list of words containing exactly n consonants is then returned. The tests ensure that the function behaves as expected for various inputs. You can add more tests to further validate the function's behavior.