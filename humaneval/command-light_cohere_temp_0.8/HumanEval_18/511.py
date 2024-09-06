```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string, without overlapping.
    return: 
    counter = 0
    start = 0
    for i, char in enumerate(string):
        if char == substring:
            counter += 1
        if counter == len(substring):
            return i+start
    return -1

# Test cases
test_1 = ("aaa", "aa")
test_2 = ("aaaa", "aa")
test_3 = ("ababb", "ab")
test_4 = ("abc", "a")
test_5 = ("aabac", "aa")
test_6 = ("abcda", "cd")

for test, expected in [(test_1, 0), (test_2, 3), (test_3, 2), (test_4, 1), (test_5, 2), (test_6, 1)] 

``` 
This code defines a Python function that finds the occurrences of a substring in a given string, without overlapping. It uses a counter to keep track of the occurrences, and returns the starting index when the substring is found. 
The function also includes test cases to validate its behavior.