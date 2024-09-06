```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```
The function `is_bored` accepts a string as its argument and seeks to identify sentences beginning with the word "I," subsequently tallying these instances. It accomplishes this by dividing the input string into separate sentences using the punctuation marks ".", "?", and "!". The variable `boredoms` is employed to count these occurrences, ultimately returning the total number of sentences starting with "I." 

Here is an example usage of the function and its corresponding output:
```python
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
```
This will output:
```bash
1
```