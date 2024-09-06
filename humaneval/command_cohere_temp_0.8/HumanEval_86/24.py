```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as the delimiter, then iterates through each word. For each word, it sorts the characters alphabetically based on their ASCII values and joins them back together into a new word. This new word is then added to the `new_word_array`. Finally, the function returns a space-separated string composed of the newly created words, maintaining the original word order and spacing.

This solution adheres to the problem statement and produces the expected output while maintaining efficiency by leveraging Python's built-in sorting and string manipulation functions. Below is a simple test case to verify the functionality of the provided solution:
```python
def test_anti_shuffle():
    assert anti_shuffle("Hi") == "Hi"
    assert anti_shuffle("hello") == "ehllo"
    assert anti_shuffle("Hello World!!!") == "Hello !!!Wdlor"

test_anti_shuffle()
```