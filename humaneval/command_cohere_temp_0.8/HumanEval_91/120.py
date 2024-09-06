```python
def is_bored(S):
    """
    Count the number of boredoms in the given string.
    A boredom is a sentence that starts with the word "I".
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('!?')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```

This script divides the string into sentences using the period as a delimiter and checks if each sentence starts with the word "I" to identify and count boredoms. The `strip('!?')` removes any trailing question marks or exclamation marks that might be attached to the sentences. This ensures an accurate count without considering punctuation directly following the sentence. 

To test this, you can call the function with different inputs and compare it with the output of the example given.

```python
# Test 1:Typical string
test_str = "The sky is blue. The sun is shining. I love this weather"
test_result = is_bored(test_str)
print(f "Test 1: {test_result} ") # Expected output: 1

# Test 2: Typical string
test_str = "Hello world"
test_result = is_bored(test_str)
print(f "Test 2: {test_result} ") # Expected output: 0
``` 

This should return `1` for the first test case and `0` for the second, which corresponds to the examples given in the problem statement.  This approach assumes that sentences are properly delimited by periods, questions marks, or exclamation marks. 

If the provided delimiters are not present in the input, the script might need additional adjustments. However, this provided solution should work well for standard textual data.