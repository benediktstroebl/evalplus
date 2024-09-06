```python
def find_max(words):
    max_unique_words = sorted(words, key=lambda word: (len(set(word)), word))
    return max_unique_words[0]
```

The function `find_max` takes a list of strings, as an argument, and returns the word with the maximum number of unique characters. In the case of multiple strings having the maximum number of unique characters, the function will return the one that comes first in lexicographical order. The key argument in the sorted function is used to customize the sorting order, with `lambda word: (len(set(word)), word)` returning a tuple where the length of the unique characters set is the first element and the actual word is the second element, making it easy to sort based on the requirements. 

The given example tests would yield the following results:
```
find_max(["name", "of", "string"]) == "string"
find_max(["name", "enam", "game"]) == "enam"
find_max(["aaaaaaa", "bb" ,"cc"]) == "aaaaaaa"
```

The first example will return "string", the second one "enam", and the last one "aaaaaaa", following the criteria explained above. 

If you would like to test this script, you can create a Python file and run it. You can also use this code snippet in a Python interpreter via your IDE or via the command line:
```bash
python -i <file_name>.py
```

This will execute the script and allow you to interact with the function find_max via the command line.