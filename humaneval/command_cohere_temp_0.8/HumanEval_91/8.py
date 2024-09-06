Here's a Python script with a self-contained function that solves the problem:
```python
def is_bored(S):
    count = 0
    for sentence in S.split('.'):
        sentence = sentence.strip()
        if sentence.startswith('I'):
            count += 1
    return count
```

This function iterates through each sentence in the input string, and if a sentence starts with the word 'I', it increments the count variable. Finally, the function returns the count variable.

Here's how some example inputs wrap out in tests to ensure the function behaves as expected:
```python
# TEST 1: Simple case
test_cases = [
    ("Hello world"),
    ("The sky is blue. The sun is shining. I love this weather"),
    ("?? Hello world! I feel angry. I am frustrated."),
]

for case in test_cases:
    assert is_bored(case) == 1
``` 

This test case ensures that the function returns 1 for a sentence that starts with the word 'I'.