```python
def split_words(txt):
    words = txt.split(',') if txt.find(' ') == -1 else txt.split()
    return words if words != ',' else len(list(filter(lambda x: x in str.ascii_lowercase, txt)))
```
The problem prompts us to return the number of lowercase letters with odd order in the alphabet if the given string does not contain any whitespace or comma separators. We achieve this using the filter and len functions, filtering all lowercase letters from the string and returning the length of the resulting list. The filter function takes a function or lambda expression as an argument and returns a list of elements for which the function returns True. In this case, we want to filter all characters that are lowercase letters, which can be achieved with the lambda expression lambda x: x in str.ascii_lowercase. The in operator checks if a value is present in a container (in this case, the str.ascii_lowercase container), and the expression x in str.ascii_lowercase returns True if x is an ASCII lowercase letter, and False otherwise. The resulting list with all lowercase letters is then returned, and the len function applies to this list to return the number of elements in the list. 

The logic of the code can be tested independently from the main function using unit tests, which are small functions that invoke the function of interest with different inputs and validate that the output matches the expected output. Below is an example of how these tests could look:
```python
def test_split_words():
    assert split_words("Hello world!") == ["Hello", "world!"]
    assert split_words("Hello, world!") == ["Hello", "world!"]
    assert split_words("abcdef") == 3
    assert split_words("abcdefg") == 3
    assert split_words("abcd,efg") == 3
    assert split_words("pale,blue") == 3
    assert split_words("pale blue") == ["pale", "blue"]
    assert split_words("abc") == 3
    assert split_words("abc,") == 3
    assert split_words(",") == 0
``` 

This script contains multiple functions, with test_split_words() being the one that invokes split_words() and asserts (using the assert statement) that the output of the function matches the expected output for each of the different inputs. The name of each test is a brief description of what is being tested, and the inputs and assertions are inside the parenthesis. Because the tests are run independently from the original code, they can be used to verify the code logic in different versions of the function or even in completely different code libraries, as long as the function signature stays the same. 

In this case, the signature of the function is (txt: str) -> int, with the int and str types being the parameters and constraints on the input and output of the function, respectively.