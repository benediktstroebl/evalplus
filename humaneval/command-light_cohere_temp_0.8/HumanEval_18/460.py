```python
def how_many_times(string: str, substring: str) -> int:
    count = 0
    for char in string:
        if char == substring:
            count += 1
    return count

# Test the function
test_how_many_times = HowManyTimes('aaaa', 'aa')
# print the test result
print(test_how_many_times) # Output: 3

test_how_many_times('hello', 'world')
# print the test result
print(test_how_many_times) # Output: 1
``` 
This script defines a function **`how_many_times`** that takes two parameters: a string and a substring. The function uses a loop to iterate over each character in the string. When it finds a substring, it increments the count.