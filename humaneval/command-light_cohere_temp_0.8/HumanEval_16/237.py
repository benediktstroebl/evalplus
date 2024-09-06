```python
def count_distinct_characters(string):
    """
    Count distinct characters, ignoring case.
    Return the count of unique characters in the given string,
    ignoring upper and lower case.
    """
    print(string.count_distinct_characters("Hello World"))
    print(string.count_distinct_characters("jerry"))
    print(string.count_distinct_characters("jERry"))
    print(string.count_distinct_characters("hello world"))
    print(string.count_distinct_characters(" j_erry "))
    print(string.count_distinct_characters("J_IS_FOOL"))
    print(string.count_distinct_characters("123"))
    print(string.count_distinct_characters("abc"))
    print(string.count_distinct_characters("abcXYZ"))
    """

Returns: number of distinct characters.

# Testing the function with some inputs
print(count_distinct_characters("jerry")) # Should return 4.
print(count_distinct_characters("hello world")) # Should return 10
print(count_distinct_characters("ABC")) # Should return 3
print(count_distinct_characters("123")) # Should return 4
print(count_distinct_characters("abcXYZ")) # Should return 5
```