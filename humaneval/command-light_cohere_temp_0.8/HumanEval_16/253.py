```python
def count_distinct_characters(string: str):
    return len(set(string.isalpha())))
```

This function computes and returns the count of distinct characters in the string, regardless of case. The function uses the str.isalpha() method to convert all characters in the string to lowercase and then converts all strings into a set. This set is distincts the characters back to their original case. 

Here's how the code works:
1. Creating a function named count_distinct_characters that takes a string as an argument.
2. Converting all characters to lowercase using the str.isalpha() method.
3. character and count the a distinct set of characters in the string.
4. Return the count of distinct characters in the string, which is the length of the set.

Here are some test cases:
```python
# Test case 1
test_string = "xyzXYZ"
assert count_distinct_characters(test_string) == 3

# Test case 2
test_string = "Jerry"
assert count_distinct_characters(test_string) == 4
```

These test cases verify that the function correctly calculates the number of distinct characters in different input strings.