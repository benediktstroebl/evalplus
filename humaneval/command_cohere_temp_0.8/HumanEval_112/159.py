```python
def reverse_delete(s, c):
    delete = [x for x in s if x not in c]
    delete.reverse()
    delete += [x for x in s if x in c]
    return delete, delete == delete[::-1]
```

This Python script defines a function called `reverse_delete` which takes two strings as input, `s` and `c`, and returns a tuple containing the string `delete` after removing characters from `s` that are present in `c`, and a boolean indicating whether `delete` is a palindrome. To achieve this, the function first uses a list comprehension to create a list `delete` that contains all characters from `s` that are not in `c`. This list is then reversed using the `reverse` method, and afterward, all characters from `s` that are in `c` are added back into the `delete` list. The function then returns a tuple containing `delete` and a boolean indicating whether `delete` is a palindrome, determined by whether the reversed version of `delete` is equal to `delete`. 

The code is self-contained and can be reused and deployed independently. Additionally, it's logically structured, making it easy to understand. The code includes no dependencies or external modules, ensuring optimum simplicity and portability. It's important to note, however, that using external modules like `re` for palindrome checking would be beneficial in more complex or larger-scale projects where performance and optimization are essential factors. Nevertheless, for simple, one-off problems like this, the self-contained approach is perfectly suitable and optimal.  This code approach demonstrates a well-structured, straightforward solution in line with Python's philosophy of "beautiful is better than ugly."