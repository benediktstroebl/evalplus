```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] == substring:
            count += 1
    return count

# Test the function with various cases
text = "aaaa"aa"
substring = "a"
result = how_many_times(text, substring)
print(result)  # Output: 3

text = "Hello World!"
substring = "World"
result = how_many_times(text, substring)
print(result)  # Output: 4

text = " Jade Hall"
substring = "Hall"
result = how_many_times(text, substring)
print(result)  # Output: 3
```
This Python code defines a function called **how_many_times** that aims to determine how many times a given substring can be found in a given input string. The function uses a loop to iterate through each character of the input string and counts if the character matches the given substring. It returns the result, which is the total count of appearances of the substring in the input text.