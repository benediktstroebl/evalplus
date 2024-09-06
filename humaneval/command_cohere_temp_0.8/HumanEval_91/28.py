```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    num_boredoms = 0
    current_boredom = False
    for word in S.split():
        if word == 'I':
            current_boredom = True
        elif word in ['.', '?', '!'] :
            if current_boredom :
                num_boredoms += 1
            current_boredom = False
    return num_boredoms
```

This script splits the input string by space into a list of words, and then traverses this list. The variable `current_boredom` is a boolean variable that indicates whether the current sentence starts with the word 'I', which indicates a potential boredom. Whenever the script encounters a sentence end, indicated by finding one of '.', '?', or '!', if `current_boredom` is True, it increments the `num_boredoms` counter. The script then resets `current_boredom` to False to reset the state for the next sentence. 

The script is a self-contained Python function that can be imported and run independently, and should pass the given tests.