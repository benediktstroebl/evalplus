```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```

This approach splits the input string on '.' characters, strips off !? characters from the ends of the segments, and checks if the resulting string starts with the word 'I'. 

Here's some example usage:
```python
# Test cases
print( is_bored("Hello world") )  # Count should be 0 for this case
print( is_bored("The sky is blue. The sun is shining. I love this weather") )  # Count should be 1 for this case
print( is_bored("?Hello world! How are you.?") )  # Count should be 0 for this case
```

This should output:
```
0
1
0
```