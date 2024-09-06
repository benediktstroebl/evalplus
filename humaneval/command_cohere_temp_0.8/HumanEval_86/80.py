```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string, where each word is sorted by ASCII value. The function first splits the input string into individual words using the `split()` method. Then, it iterates through each word in the list and sorts the characters in that word from lowest to highest ASCII value, using the `sorted()` function. The sorted word is then appended to the `new_word_array`. Finally, the function joins the newly sorted words back into a single string with spaces in between, using the `join()` method, and returns the resulting string.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

And another one to further illustrate the functionality:
```python
print(anti_shuffle("ehllo")) # output: "hello"
```