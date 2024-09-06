```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

The function `anti_shuffle` takes a string as input and returns a sorted version of the string where each word's characters are arranged in ascending order based on their ASCII values. The function first splits the input string into individual words and stores them in the `word_array` list. Then, it iterates through each word in the list, sorts its characters alphabetically, and stores the sorted word in the `new_word_array` list. Finally, the function joins the sorted words back together with spaces between them and returns the ordered version of the input string.

Here is an example function call:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```