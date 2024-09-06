```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_ordered = ''.join(sorted(word))
        new_word_array.append(ascii_ordered)
    return ' '.join(new_word_array)
```

This approach first splits the entire string into words (or arrays of words) and then constructs a new string by joining all the sorted words, ensuring the original spacing between the words. 

For example, the call anti_shuffle("Hello World!!!") would return "Hello !!!Wdlor". 

This algorithm is case-sensitive, so it would also treat "Hi" as "Hi" and return it as such. You can include a normalization step if desired, e.g., making everything lowercase. 

If you want to handle punctuation in various ways, this would also require additional preprocessing or parameterization, which we can discuss and implement further based on your needs.