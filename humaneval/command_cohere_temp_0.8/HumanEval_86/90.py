Here's a Python script with a self-contained function that solves the anti-shuffle problem as described in the markdown code block:
```python
def anti_shuffle(s):
    words = s.split()
    new_word = ''.join(sorted(words[0]))
    for word in words[1:]:
        new_word += ' ' + ''.join(sorted(word))
    return new_word
```
This script splits the input string `s` into a list of words using the `split()` method. Then, it iterates through each word using a loop and sorts each word based on the ASCII value of each character. The sorted characters are then joined back together to form the new word. The process is repeated for each word in the list, and the sorted words are finally reassembled with appropriate spaces in between to form the `new_word`. The function returns this ordered version of the input string.

Here's an example usage of the function for the input `'Hello World!!!'`**:
```python
print(anti_shuffle('Hello World!!!'))
```
**Output:**
```
Hello !!!Wdlor
```

This example demonstrates the function's ability to maintain the order of words and spaces while rearranging the characters within each word based on their ASCII values.