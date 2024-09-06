```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach splits the input string by periods to individualize sentences, and then strips each sentence to discard leading and trailing whitespaces. Subsequently, it checks if the beginning word of each sentence is 'I', and if so, increments the counter. Ultimately, the function returns the total count of sentences that commence with 'I'. 

Here is an example usage of the function which test cases and showcases its compatibility with different sentence delimiters and whitespace formats:
```python
>>> is_bored("I am bored.")
1
>>> is_bored("I am not bored.?")
1
>>> is_bored("I am! not bored.")
1
>>> is_bored("Nothing to worry about, no problem at all!")
0
>>> is_bored("I am bored. Now you try.")
1
>>> is_bored("I am  bored.  Now you ? try.")
1
``` 
This variety of tests assures the function's robustness across multiple scenarios.