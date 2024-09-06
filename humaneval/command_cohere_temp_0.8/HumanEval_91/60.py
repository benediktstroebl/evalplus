```python
def is_bored(S):
    boredom_count = sum(1 for sentence in S.split('. ') if sentence.strip()[0] == 'I')
    return boredom_count
```

This script defines a function, `is_bored`, which takes a string as an input and returns the number of boredoms in the string. This is achieved through the use of a generator expression that splits the input string into sentences and identifies and counts the instances of 'I' at the beginning of each sentence. The sum function is then used to aggregate the counts into a single number, representing the total number of boredoms in the given input string.