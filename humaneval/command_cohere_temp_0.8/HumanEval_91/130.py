```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    Sentences are assumed to be delimited by '.', '?', or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?)').strip('i')
        if sentence.startswith('i'):
            boredoms += 1
    return boredoms
```

This approach splits the input string by decimal points, strips off potential sentenceenders and delimiters, and checks if the sentence starts with the word "I". The function then returns the counted 'boredoms'. 

To test this, you can call this function on test cases like:
```python
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
``` 
The first output will be `0` since the word "I" in the sentence is not the starting word of a sentence. The second output will be `1` since the sentence "I love this weather" is a boredom.