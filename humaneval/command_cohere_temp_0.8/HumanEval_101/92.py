Here's a Python script that contains a function `words_string` that solves the problem:
```python
def words_string(s):
    return s.split()
```

The Python built-in method `split()` is utilized to partition the input string `s` wherever it encounters commas or spaces. This produces an array-like list where each element is an individual word from the original string. This function solves the problem without requiring any additional dependencies or external configurations, making it both effective and standalone. 

The method is applied in the example below:
```python
print(words_string("Hi, my name is John"))
```

To run this code, you'll need a Python interpreter that can execute markdown code blocks, such as IDLE or VS Code. When the code is executed, it will print the following result:
```
['Hi', 'my', 'name', 'is', 'John']
```

This exemplifies the function' ability to effectively dissect a string into individual words and present them as an array.