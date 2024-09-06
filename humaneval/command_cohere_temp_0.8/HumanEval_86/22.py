```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (assuming words are separated by spaces) and then sorts each word based on the ascii values of its characters, thus, preserving the order of words and blank spaces. The output will be the input string with each word replaced by its sorted counterpart. 

Here's a usage example:
```python
print(anti_shuffle("Hello World!!!")) # output: "Hello !!!Wdlor"
```

This will output: "Hello !!!Wdlor" which is the ordered version of the string where each word is replaced by its sorted counterpart.