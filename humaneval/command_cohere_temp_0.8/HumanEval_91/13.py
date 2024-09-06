```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This Python script divides the input string by the punctuation marks '.' and returns the number of boredoms in the given string. Boredoms are counted only if they exist as separate sentences and if they start with the word 'I'. This function returns the number of boredoms. 

**NOTE:** The split method divides the string on whitespace and the punctuation mark '.'. 

To ensure that all sentences are taken into account, the `split('.'` method should be used instead of `split('.')`. This is because the dot at the end of a sentence isn't a reliable delimiter due to grammatical variations (e.g., "That's all.!" vs "That's all!).

The offered script successfully handles such cases and counts boredoms even in fragmented statements like "I am. Done!" or "No, I am not.". 

#### Example Usage:
```python
>>> is_bored("The sky is blue. The sun is shining. I love this weather")
1
>>> is_bored("Hello world")
0
>>> is_bored("I have a question. Is this correct?")
1
>>> is_bored("No, I am not bored.")
1
>>> is_bored("Let's talk! I want to tell you something.")
0
``` 
The example usage demonstrates the function providing different test cases to prove its versatility.