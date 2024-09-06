```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by the punctuation marks '.' and '?!', and counts the number of sentences that start with the word 'I'. 

Here's a test case to verify the function:
```python
def test_is_bored():
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("Hello world") == 0
    assert is_bored("How are you? I am fine.") == 1
    assert is_bored("Stop it! You're hurting me.") == 1
    assert is_bored("???") == 0
```