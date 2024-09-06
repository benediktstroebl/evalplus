```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Returns the number of vowels in a string s,
    including special case for y as a vowel at the end of the word."""
    vowels = 'AEIOUaeiou'
    return sum(1 for i,let in enumerate(s) if let in vowels and (let!='Y' or i==len(s)-1))
```