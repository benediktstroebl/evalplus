Here's a Python script with a self-contained function that solves the problem:
```python
def same_chars(s0, s1):
    return len(set(s0) & set(s1)) / min(len(s0), len(s1)) > 0.6
```
The function determines whether two strings have a substantial amount of overlapping characters by comparing the intersection of their character sets to the length of the shorter string. It returns True when the percentage of overlapping characters exceeds 0.6, indicating that the words share many characters, and can be additionally evaluated using the provided test cases. Adjust the threshold percentage as needed to adapt to different cases. 
```python
def test_same_chars():
    """
    Test the same_chars function
    """
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddeddabc') == True
    assert same_chars('abcd', 'dddddddabc') == True
    assert same_chars('dddddddabc', 'abcd') == True
    assert same_chars('eabcd', 'dddddddabc') == False
    assert same_chars('abcd', 'dddddddabce') == False
    assert same_chars('eabcdzzzz', 'dddzzzzzzzddddabc') == False
```

You can use this script to test the function with different inputs. Adjust the test cases in the test_same_chars function to cover more scenarios and ensure the function's correctness.