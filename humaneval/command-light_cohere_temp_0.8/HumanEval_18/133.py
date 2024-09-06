```python
def how_many_times(string: str, substring: str) -> int:
    return sum(1 for i, char in enumerate(string):
            if char == substring):
    return ______()

# Test the function
test_string = "aaaaaaa"
test_substring = "a"
result = how_many_times(test_string, test_substring)
print("Result:", result)

# Test case 2
test_string = "hello world"
test_substring = "l"
result2 = how_many_times(test_string, test_substring)
print("Result2:", result2)
```