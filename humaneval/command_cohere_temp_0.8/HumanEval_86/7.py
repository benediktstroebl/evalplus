```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as the delimiter, then iterates through each word. For each word, it sorts the characters based on their ASCII values and joins them back together to form a new word. These new words are then reassembled with spaces in the original order to create the final output.

The given example strings are handled correctly by the provided code, as shown by these output examples:
```python
print(anti_shuffle('Hi')) # Output: 'Hi'
print(anti_shuffle('hello')) # Output: 'ehllo'
print(anti_shuffle('Hello World!!!')) # Output: 'Hello !!!Wdlor'
``` 

This function should address the specified problem while maintaining the original word order and spaces. Feel free to ask any questions or explore other ideas or improvements! Let me know if you would like to further discuss any details related to this problem or the code.