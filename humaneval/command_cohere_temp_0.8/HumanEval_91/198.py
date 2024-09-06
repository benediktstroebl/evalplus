Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This script defines a function `is_bored` that takes a string as an input and counts the number of boredoms in the string. The function uses a for loop to iterate over each sentence (assuming they end with a '.') in the input string and checks if each sentence starts with 'I'. If so, it increments the counter and returns the count of boredoms after processing all the sentences. The `strip` function is used to remove any whitespace at the beginning and end of each sentence.

To use this script for the provided tests, just call the function with the relevant input strings as follows:
```python
# The sky is blue. The sun is shining. I love this weather
result = is_bored("The sky is blue. The sun is shining. I love this weather")
print(result)  # Output: 1

# Hello world
result = is_bored("Hello world")
print(result)  # Output: 0
``` 

This will return 1 for the first input string and 0 for the second, which aligns with the examples provided in the problem statement. 
*Note*: this approach assumes that each sentence in the input string ends with a '.'.  If the input might include sentences with different end punctuations ('?', '!' or others), additional logic would be necessary to accurately split the sentences.