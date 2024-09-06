```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set()
    for i in range(len(s)-2):
        if len(set([s[i], s[i+1], s[i+2]])) != 3:
            return False
    return True
```

This script defines a function called `is_happy` that takes in a string as an input and checks whether the string is happy or not. The function returns `True` if the string is happy, and `False` otherwise. 

The function first checks if the length of the string is at least 3, and returns `False` if it's less than 3 since all strings of length one and two are not happy, no matter what letters they contain. Then, it proceeds to check if every set of 3 consecutive letters are distinct. It achieves this by using a `set` to store letters that have been previously encountered, to check if each letter is unique within each set of 3 consecutive letters. If the length of the resulting set is not equal to 3, it returns `False`, else returns `True`. 

Overall, this code correctly checks the happiness of the string as described in the problem statement. 

You can test this script with sample strings to cover different cases like `happy` and `not_happy` strings. Here is an example: 
```python
# Testing the is_happy function
# Happy Cases
print(is_happy("abcd")) # True
print(is_happy("xyab")) # True
print(is_happy("qwertyuiop")) # True

# Not Happy Cases
print(is_happy("aaa")) # False
print(is_happy("abbb")) # False
print(is_happy("bcdd")) # False
``` 

This will produce the following output:
```
True
True
True
False
False
False
``` 
This confirms that the `is_happy` function is correctly solving the problem.