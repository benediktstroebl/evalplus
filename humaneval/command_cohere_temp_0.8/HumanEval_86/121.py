```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        char_array = list(word)
        char_array.sort()
        new_word = ''.join(char_array)
        new_word_array.append(new_word)
    return ' '.join(new_word_array)
```

The code splits the input string into a list of words and then iterates through each word. For each word, it creates a list of characters, sorts them alphabetically based on their ASCII values, and then joins them back to form a new word. These new words are accumulated in another list and then rejoined with spaces to form the final output string.

The given example tests cases are correctly handled by the provided code:
```python
def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

test_anti_shuffle()
```