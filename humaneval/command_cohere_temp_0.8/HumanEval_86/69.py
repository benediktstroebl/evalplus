```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This Python script defines a function `anti_shuffle` that takes a string as an input and returns a sorted version of the string. In the function, the input string is split into an array of words, and an empty array is created to hold the sorted versions of each word. Then, in the loop, each word is sorted based on ASCII values and appended to the new_word_array. Finally, the function returns a string where the newly sorted array words are joined with spaces.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```