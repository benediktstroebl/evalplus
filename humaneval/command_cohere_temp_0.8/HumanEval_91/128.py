```python
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    boredoms = 0
    for sentence in S.split('.'):
        sentence = sentence.strip('?')
        sentence = sentence.strip('!')
        if sentence.startswith('I'):
            boredoms += 1
    return boredoms
```

This approach splits the input string on periods, strips off any exclamation marks, and trims off any question marks, to ensure that the function can handle multiple sentence structures, including those that start with periods, exclamation marks, or question marks. It then checks if the trimmed sentence starts with the word "I", and if so, it increments the counter. Finally, it returns the count of boredoms found in the string. 

To employ this code in the problem, simply call the function with your input string and it will return the number of boredoms. 
If you would like to test this script, you can add test cases in the same file to verify its performance on different inputs. For proper testing, it's best to include a range of scenarios encompassing different sentence structures, punctuations, and spelling variations of the word "I". 
Here's an example: 
```python
# Test 1: Basic case
test_case = "The sky is blue. The sun is shining. I love this weather"
expected_result = 1
actual_result = is_bored(test_case)

# Test 2: Case with no boredoms
test_case = "Hello world"
expected_result = 0
actual_result = is_bored(test_case)

# Test 3: Case with multiple boredoms and different punctuations
test_case = "I love cupcakes! I hate donuts. I prefer muffins."
expected_result = 2
actual_result = is_bored(test_case)

# Test 4: Case with sentences starting with "I" but lacking punctuation
test_case = "I love apples I hate oranges"
expected_result = 2
actual_result = is_bored(test_case)

```

This way you can confidently confirm that the function handles various scenarios without any unexpected errors.