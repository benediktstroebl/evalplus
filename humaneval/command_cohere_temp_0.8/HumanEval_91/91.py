```python
def is_bored(S):
    bored = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            bored += 1
    return bored
```

This approach breaks the input string into separate sentences by splitting it at each period (`.`) and then checks if each sentence starts with the word "I". The resulting count of such sentences is returned as the result. 

This code is straightforward and correctly solves the problem but may not handle some edge cases like sentences starting with "I" without a period or exclamation/question mark to delimit it as a new sentence. 

If you were to tackle this problem in a more robust manner, you could consider reifying the notion of a sentence, perhaps using libraries like `nltk` to ensure that sentences are correctly parsed even in complex cases. 

To test this script, you can call the function with different input strings and compare the output with the expected results. Here is an example: 
```python 
# Test 1: Basic case
S = "The sky is blue. The sun is shining. I love this weather"
print(is_bored(S))  # Expected output: 1

# Test 2: No boredom
S = "Welcome to this beautiful day!"
print(is_bored(S))  # Expected output: 0
``` 

This will help ensure that the function is working correctly and returning the expected results.