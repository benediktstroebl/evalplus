```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as the delimiter, and then iterates through each word. For each word, it sorts the characters based on their ASCII values and joins them back together to form a new word. These new words are then reassembled with spaces in between to form the ordered version of the input string, where each word is sorted alphabetically. 

Here is an example:
```python
print(anti_shuffle("Hello World!!!")) # Output: "Hello !!!Wdlor"
```

This will output the ordered version of the string "Hello World!!!", which is "Hello !!!Wdlor", where the words have been sorted alphebetically.