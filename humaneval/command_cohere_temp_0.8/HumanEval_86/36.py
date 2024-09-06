```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using `split()` and then for each word, it arranges the characters in ascending order based on ASCII and joins them to create a new word. It then joins these new words to form the final ordered version of the input string, keeping the original word placements and spaces. 

Here's a usage example:
```python
print(anti_shuffle("Hello World!!!"))  # Output: "Hello !!!Wdlor"
```

This will output the ordered version of the string where each word has its characters sorted by ASCII value, while maintaining the original word placements and spaces.