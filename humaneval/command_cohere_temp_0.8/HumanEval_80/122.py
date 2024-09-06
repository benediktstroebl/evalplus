```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_count = [0] * 128
    for letter in s:
        letters_count[ord(letter)] += 1
    for i in range(0, len(s), 3):
        if letters_count[ord(s[i])] > 1 or letters_count[ord(s[i+1])] > 1 or letters_count[ord(s[i+2])] > 1:
            return False
    return True
```

The algorithm to solve the problem consists of two main parts:
1. We ensure that the string length is at least 3 using the `len(s) < 3` condition.
2. We then check if any of the consecutive triplets of letters appear more than once in the string. We achieve this by counting the occurrence of each letter using a 128-length array `letters_count` where each index corresponds to a letter's ASCII value. We then iterate over the string in increments of 3 and check if any of the trips can be found more than once in `letters_count`.

Such an approach results in a time complexity of `O(n)` where `n` is the length of the string and a space complexity of `O(1)`. Even though the array `letters_count` takes 128 bytes of space, it still is a constant amount of space regardless of the input size.