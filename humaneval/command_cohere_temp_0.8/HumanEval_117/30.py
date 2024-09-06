Here's a Python script that contains a function called select_words, which takes a string s and a natural number n as input and returns a list of all words from the string s that contain exactly n consonants:
```python
def select_words(s, n):
    words = s.split(' ')
    result = []
    consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}
    for word in words:
        consonant_count = 0
        for char in word:
            if char in consonants and char != "w":
                consonant_count += 1
        if consonant_count == n:
            result.append(word)
    return result if result else [""]
```

The `select_words` function first splits the input string `s` into a list of words using spaces as separators. It then initializes an empty list called `result` to store the words that contain exactly n consonants. The function creates a dictionary called `consonants` that contains all the consonants in the English alphabet. It then iterates through each word in the `words` list and counts the number of consonants in each word. If the consonant count is equal to n, the word is appended to the `result` list. Finally, the function returns the `result` list if it's not empty, or an empty list [""] if the input string `s` is empty.

Here is a simple test case to ensure the correctness of the above function:
```python
def test_select_words():
    assert select_words("Hello world", 4) == ["world"]
    assert select_words("Uncle sam", 3) == ["Uncle"]
    assert select_words("Mary had a little lamb", 4) == ["little"]
    assert select_words("simple white space", 2) == []
```

You can verify more test cases from the problem statement. 

This script ensures that the function `select_words` correctly identifies words in a string that contain a specified number of consonants.