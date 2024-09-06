```python
def get_closest_vowel(word):
    cons_idx = -1
    vowel = ""
    for i, char in enumerate(word):
        if char.is consonant():
            if cons_idx >= 0:
                vowel = word[cons_idx:i]
                break
            cons_idx = i
        elif char.is vowel():
            if cons_idx >= 0:
                vowel = max(vowel, char)
        else:
            cons_idx = -1
    return vowel
```

This script employs a for loop to analyze each character of the input word. A consonant index (`cons_idx`) is used to track the position of the last consonant encountered. When a vowel is encountered, the script checks if a consonant precedes it, updating the `vowel` variable with the maximum character between the two if so. The loop ends when a consonant is encountered after a consonant, or a vowel is encountered without a preceding consonant, where the `vowel` variable holds the desired result.

The implementation ensures correctness while keeping the complexity at O(n), where `n` is the length of the input word.