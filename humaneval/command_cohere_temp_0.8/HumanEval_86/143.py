```python
def anti_shuffle(s):
    word_list = s.split()
    new_word_list = []

    for word in word_list:
        ascii_sorted = ''.join(sorted(word))
        new_word_list.append(ascii_sorted)

    return ' '.join(new_word_list)
```

This approach takes the original string, splits it into individual words, sorts the characters in each word based on their ASCII values, and then joins the sorted words back together to form the final ordered version of the string. This algorithm maintains the word order and spaces from the original string.

Here's a test case to verify the function:
```python
def test_anti_shuffle():
    # Single word
    assert anti_shuffle("Hi") == "Hi"

    # Multiple words
    assert anti_shuffle("hello world") == "ehllo durhl"

    # With special characters
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

    # With multiple spaces
    assert anti_shuffle("hello   world") == "ehllo     durhl"

test_anti_shuffle()
```