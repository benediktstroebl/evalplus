```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    num_boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            num_boredoms += 1
    return num_boredoms
```
This script defines a function called `is_bored` that takes in a string as an argument and counts the number of boredoms in the string. It separates the input string into sentences by splitting it using the '.' character. It then removes the punctuation marks '!' and '?' from the end of each sentence. After that, it checks if the sentence starts with the word 'I', and if it does, it counts it as a boredom. Finally, it returns the total count of boredoms in the input string. 
This solution complies with the problem statement by counting the number of boredoms in the input string and returning the total count of sentences that start with the word "I."