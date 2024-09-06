```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string, where each word is sorted by ASCII value. The function first splits the input string into individual words using the `split()` method. Then, it iterates through each word in the list and sorts the characters in that word from lowest to highest ASCII value, using the `sorted()` function. The sorted word is then added back into the list, and finally, the function joins the list of new words back into a single string, using blank spaces as the delimiters.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will return the ordered version of the string "Hello World!!!", where each word is sorted by the ASCII value of their characters.