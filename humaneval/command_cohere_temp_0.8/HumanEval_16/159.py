Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters and converts the input string to lowercase to ensure that uppercase and lowercase characters are treated the same. The test cases provided will verify that the function behaves as expected. 

Here's how you can execute this script and run the tests:
```bash
$ python script.py
```
This will run the tests and print out the results, verifying that the function `count_distinct_characters` satisfies the problem statement.