```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string without changing the word order in the string. In the provided example, the output for `anti_shuffle('Hello World!!!')` would be `'Hello !!!Wdlor'`, which is correct. 

This algorithm utilizes Python's built-in sorted function to keep the letter arrangement sequential in ascending order, irrespective of the word order. To achieve this, the function first splits the input string into an array of words, ignoring the spaces, and then uses Python's join function to combine the sorted letters of each word into a new line-separated array. The resultant array is then returned as a string, with the word order maintained from the original input string.