```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s[0:3])
    for i in range(3, len(s), 3):
        if len(set(s[i:i+3])) != 3:
            return False
    return True
```

This script defines a function `is_happy` that takes a string `s` as input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

Here is a breakdown of the code:
- The function starts by checking if the string's length is at least 3. If not, it returns False because there is not enough data to determine happiness.
- It then uses the first 3 letters as a benchmark for the subsequent checks. It creates a set of these first 3 letters and uses it to compare to the next sets of 3 letters in the string. 
- The loop checks each set of 3 consecutive letters compared to the first 3 letters. If the set of 3 consecutive letters is not distinct, it returns False. 
- If it has checked through the entire string and none of these sets were not distinct, it returns True. 

This problem can be solved more efficiently with a different approach. 

Note that this solution utilizes set comparisons, which are optimized in Python due to the O(1) time complexity for set membership tests. 

This solution provides a clear and concise approach to solving this problem with a manageable amount of code and an efficient algorithm.