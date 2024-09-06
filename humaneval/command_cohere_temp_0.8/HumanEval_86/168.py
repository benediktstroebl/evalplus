```python
def anti_shuffle(s):
    word_array = s.split()
    new_word_array = []
    for word in word_array:
        ascii_sorted = ''.join(sorted(word))
        new_word_array.append(ascii_sorted)
    return ' '.join(new_word_array)
```

This approach takes the input string, splits it into words using space as the delimiter, and then sorts the characters in each word elementally (ASCII value) and anew creates a string array with sorted words. Finally, the function returns a string where the newly created word array is joined using spaces, maintaining the original word order. 

Here's an example usage interaction of the function with the input "Hello World!!!":
```python
print(anti_shuffle("Hello World!!!"))  # Output: "Hello !!!Wdlor"
```

This solves the problem statement and returns the ordered version of the input string.