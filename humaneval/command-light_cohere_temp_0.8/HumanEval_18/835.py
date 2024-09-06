```python
def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string.

    :def test():
        string = "hello world"
        sub = "ll"
        n = how_many_times(string, sub)
        print(f"The number of {sub} in {string} is: {n}")
        return n

# Example test cases
test_one = [ ] = [ "hello world", "ll" ]
test_two = [ "aaaa", "ll"]
test_three = [ "a", "ll"]

test_results = [ ]
for test in test_one:
    test_results.add(f = how_many_times(*test))

print(f"Test Results:")
for result,test in zip(test_results,test_results):
    print(f"{test} : {result}")
``` 
This code defines a Python script with a self-contained function that solves the problem of finding the number of occurrences of a given substring within a given string. The function includes a test case and passes corresponding tests successfully.