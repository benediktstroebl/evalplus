```python
def count_distinct_characters(string: str):
    return len(set(string))

# Testing the function
string1 = "xyXyzXyz"
string2 = "jerry"
string3 = ""
string4 = "Asdfasa"

print("Test 1 Result:", count_distinct_characters(string1))
print("Test 2 Result:", count_distinct_characters(string2))
print("Test 3 Result:", count_distinct_characters(string3))
print("Test 4 Result:", count_distinct_characters(string4))
```

The code defines a function `count_distinct_characters` that accepts a string as an argument and calculates and returns the count of distinct characters in that string. The function utilizes the`len` to convert the string into a set, and then uses the `len` function to get the size of the set, which corresponds to the count of distinct characters. The function is tested with four test cases: empty string, a string with no distinct characters, a string with unique characters, and a string with mixed case characters.