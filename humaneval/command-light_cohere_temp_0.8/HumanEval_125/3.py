```python
def split_words(text):
    words = ['']
    for c in text:
        if c=='':
            words.append(c)
        elif c==','':
            words.append(c)
            else:
                words[-1]+=[c]
    return words

# Tests
def test_split_words():
    assert split_words("Hello world!") == ['Hello', 'world']
    assert split_words("Hello,world!") == ['Hello', 'world']
    assert split_words("abcdef") == 3
    assert split_words(" ") == []

if __name__=='main__':
    test_split_words()
```

This Python script defines a function called **`split_words`** that takes a text input and splits it into a list of words based on whitespace. The function iterates through each character in the text string, and if the character is a space (' '), it appends it to the current word. If the character is not a space, it appends it to the end of the last word in the current word. The function effectively splits the strings that contain multiple spaces, commas, or other word characters into separate words.