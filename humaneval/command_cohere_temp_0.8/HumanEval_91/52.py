```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            count += 1
    return count
```

This approach splits the input string by periods to individualize sentences, strips any trailing and leading whitespaces, and checks if the beginning word of each sentence is 'I'. If it is, it increments the counter. Finally, the function returns the counter value.

The tests checkpoints are:
```python
# Test 1
sentence = "The sky is blue. The sun is shining. I love this weather"
assert is_bored(sentence) == 1

# Test 2
sentence = "Hello world"
assert is_bored(sentence) == 0

# Test 3
sentence = "? Who wants to grab something to eat. I am hungry!"
assert is_bored(sentence) == 1
```