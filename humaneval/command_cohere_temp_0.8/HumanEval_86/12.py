```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the words within the string, while maintaining the order of words and spaces. It does this by first splitting the input string into an array of words. Then, for each word in the array, it sorts the characters alphabetically based on their ASCII values and joins them to create a new word. It then appends this new word to the new word array and returns a space-separated string of the newly created words.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will create the ordered version of the string where each word is ordered alphabetically.