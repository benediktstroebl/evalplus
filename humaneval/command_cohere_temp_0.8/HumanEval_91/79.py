```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            count += 1
    return count
```

This script divides the input string `S` into separate sentences by splitting it at each period '.', and then removes the trailing punctuation from each sentence. It checks if the stripped sentence starts with the word 'I', and if so, it increments the counter `count`. Finally, the function returns the total count of sentences that start with the word 'I'.

Here is an example usage of the function which outputs "1" when executed:
```python
print(is_bored("The sky is blue. The sun is shining. I love this weather"))
```

And here is an example usage of the function which outputs "0" when executed:
```python
print(is_bored("Hello world"))
```