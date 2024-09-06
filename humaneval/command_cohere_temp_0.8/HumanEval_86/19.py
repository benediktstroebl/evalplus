```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as a delimiter, then iterates through each word, sorting the characters based on their ASCII values, and then joins them back to form a new word. It then returns all these new words back as a spaced-out string, maintaining the original word placements, thus achieving the desired 'anti-shuffle' effect. 

Here's a simple test case to validate the function:
```python
def test_anti_shuffle():
    # Single word
    assert anti_shuffle("Hi") == "Hi"

    # Multiple words
    assert anti_shuffle("hello world") == "ehllo ddlor"

    # With special characters
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

test_anti_shuffle()
```