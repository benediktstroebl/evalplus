Here's a Python script that contains a function called `how_many_times` which takes a string and a substring as input and returns the number of times the substring occurs within the string, including overlapping occurrences:
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
print(how_many_times('', 'a'))  # Output: 0
print(how_many_times('aaa', 'a'))  # Output: 3
print(how_many_times('aaaa', 'aa'))  # Output: 3
```

This script defines the `how_many_times` function, which takes a string and a substring as input and counts the occurrences of the substring within the string, including overlapping occurrences. It then verifies the function's behavior against three distinct cases: an empty input string, an input string with repeated 'a' characters, and an input string with repeated 'aa' characters. The function returns the expected counts for each case, reflecting the presence of the substring within the string, and its behavior is accurately depicted by the provided test cases. 
To store the number of occurrences, the `count` variable is used in the function. To compare the substring's offset within the string, the function employs a loop with an `substring_length` and `string_length` of iterations. 
The tests are contained and simple to comprehend because they are interwoven with the function definition. This approach allows for modular and maintainable code while ensuring that the function performs as anticipated. In the comments, I've also added some information to better explain how the code works.