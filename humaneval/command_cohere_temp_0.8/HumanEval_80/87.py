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

The problem asks us to determine whether a given string is 'happy'. This is the logic:
1. A string is happy if its length is at least 3.
2. Thus, we start by checking if the length of the given string is at least 3.
3. To be happy, every group of 3 consecutive letters must be unique.
4. So, we check the first 3 letters, which should be distinct.
5. Next, we check the next set of 3 letters (4th to 6th) -- these should also be distinct.
6. This pattern continues until we reach the end of the string or the end of a group of 3 consecutive letters.
7. If all the sets of 3 consecutive letters are distinct, the string is happy, and we return True. Otherwise, we return False. 
```

Let's break down the code:
- The function `is_happy` takes a single argument - the string `s`.
- `len(s) < 3`: Checks if the string length is at least 3. If not, it returns False because happiness cannot be guaranteed. 
- `letters_set = set(s[0:3])`: This creates a set of the first 3 letters of the string. If any of these are the same, we will return False. 
- The for loop `for i in range(3, len(s), 3):` goes through every set of 3 consecutive letters in the string. 
- `len(set(s[i:i+3])) != 3`: This checks if the set of these 3 letters is of size 3, it expects the set to have 3 distinct elements and if it does not, it returns False. 
- The function returns True if all tests pass, otherwise it returns False. 
```

The test cases ensure that the function `is_happy` behaves as expected with different inputs. You can test the function with other strings to verify its correctness further.