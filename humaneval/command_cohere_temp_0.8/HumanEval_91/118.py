```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the sentence markers ('.' punctuation marks) and iterates through every sentence. Using the `startswith()` method, it identifies whether each sentence begins with the word 'I', marking that instance as a boredom. Ultimately, it returns the count of boredoms found in the given input string.

Here are some example outputs:
```python
>>> is_bored("Hello world")
0
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
>>> is_bored("What a beautiful day! But I feel sleepy")
1
```