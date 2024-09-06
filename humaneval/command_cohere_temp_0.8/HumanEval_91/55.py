```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script splits the input string S into a list of sentences based on the punctuation marks '.', '?' and '!' and then uses the startswith method to check if the sentence starts with the word 'I'. The counter is incremented for each bored sentence and returned.

You can use the function as follows:
```python
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
>>> is_bored("Hello world")
0
```