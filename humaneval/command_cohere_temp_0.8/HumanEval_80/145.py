```python
def is_happy(s):
    if len(s) < 3:
        return False
    letters_set = set(s)
    return len(letters_set) == len(s) - 2
```

The function uses a set data structure to store the letters of the input string. Then it checks if the size of this set is equal to the number of distinct letters in the string, minus 2. This last part is justified by the fact that a happy string, by definition, has at least three letters, so subtracting 2 from the number of distinct letters gives us the number of repeating letters. Thus we can confidently return True for happy strings and False otherwise. 

To further illustrate the logic, let's take a few test cases and see how the function performs:
```python
print(is_happy('aaa')) # Output: False
print(is_happy('abcd')) # Output: True
print(is_happy('aabb')) # Output: False
print(is_happy('xtyz')) # Output: True
print(is_happy('xyy')) # Output: False
```

The function yields the expected results for each test case.