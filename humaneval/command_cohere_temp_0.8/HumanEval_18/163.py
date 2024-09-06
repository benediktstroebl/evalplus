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
assert how_many_times('aaa', 'aaa') == 1
```
This code defines the `how_many_times` function and provides test cases to validate its behavior against the expected outputs. 
The function works by first creating a count variable and setting it to 0. It then iterates over the string, checking each substring of length equal to the given substring's length and incrementing the count variable if they match. Finally, it returns the count variable. 

Let's break down the test cases to ensure we understand how it works:
1. `assert how_many_times('', 'a') == 0`: This test asserts that when the string is empty and the substring is 'a', the function should return 0. This is because the empty string has no 'a' substring.
2. `assert how_many_times('aaa', 'a') == 3`: This test asserts that when the string is 'aaa' and the substring is 'a', the function should return 3 because there are three instances of the 'a' substring.
3. `assert how_many_times('aaaa', 'aa') == 3`: This test asserts that when the string is 'aaaa' and the substring is 'aa', the function should return 3 due to overlapping instances.
4. `assert how_many_times('aaa', 'aaa') == 1`: This test asserts that when the string is 'aaa' and the substring is also 'aaa', the function should return 1 because there is exactly one instance of the substring.

You can use this code to confidently solve the problem and provide test cases to ensure your function remains robust and accurate. Let me know if you need anything else!