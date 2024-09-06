Here's a Python script with a self-contained function that solves the problem you've outlined, including tests:
```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    substring_length = len(substring)
    string_length = len(string) 
    for i in range(string_length - substring_length + 1):
        if string[i:i+substring_length] == substring:
            count += 1
    return count

# Test cases
assert how_many_times('', 'a') == 0
assert how_many_times('aaa', 'a') == 3
assert how_many_times('aaaa', 'aa') == 3
assert how_many_times('aaabbb', 'ab') == 2
```
This script includes a function `how_many_times` that takes a string `string` and a substring `substring` as input and calculates the number of times the substring occurs in the string, including overlapping instances. It then includes several test cases to validate the function against different scenarios. 

Note that the function assumes that the substring length is less than or equal to the main string's length. If this assumption is violated, the function will not provide correct results. You can add a validation check before the loop to ensure this condition holds. 
If the substring length is greater than the string length, the function returns 0, indicating that the substring never occurs in the string. Mention this edge case in the code commentary if it's relevant to your problem statements. 
If you encounter any further issues or have additional context, feel free to ask for further refinement!