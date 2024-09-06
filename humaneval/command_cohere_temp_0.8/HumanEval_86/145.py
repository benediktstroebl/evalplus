```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach first splits the string into words using the `split()` method. Then, we iterate through each word, sorting the characters based on their ASCII values and joining them back together into a new word. Finally, we join the newly ordered words back together with spaces to form the final sorted string.

Here is a demonstration of how the function works:
```python
print(anti_shuffle("Hello World!!!")) # Output: "Hello !!!Wdlor"
```

The function ensures that the word order remains intact while rearranging characters within each word based on ASCII values, thus achieving the desired result. Let me know if you would like me to explain any part of the code in more detail. I'm here to help!