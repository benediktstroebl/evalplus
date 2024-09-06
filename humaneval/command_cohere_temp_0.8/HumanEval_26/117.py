```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This code defines a function called `remove_duplicates` that takes a list of integers as input. It uses a set, called `seen`, to keep track of the unique elements it has encountered. It then iterates through the input list, and for each element that is not in the seen set, it adds it to both the seen set and the result list. This ensures that any element occurring more than once in the input list will only appear once in the result. As a result, the function removes duplicates and returns a unique list in the same order as the input list. 

Here's an example usage illustration:
```python
# Example usage
input_list = [1, 2, 3, 2, 4]
result_list = remove_duplicates(input_list)
print(result_list)
```

With the input list `[1, 2, 3, 2, 4]`, the output will be `[1, 3, 4]`, as explained in the docstring.  This makes the code more reusable and easier to understand, especially when multiple list cleaning operations need to be performed.  In the future, if you need to apply this function to different types of lists or perform other cleanup operations, you can easily do so without modifying the function's core logic.  This promotes the principle of separation of concerns and supports modular and maintainable code, which is a key objective of the Python programming language and its community.  If you want to learn more about best practices and methodologies for code organization, you can find many excellent resources in the Python ecosystem, such as the PEP 8 style guide and resources available on the Web.  Furthermore, if you want to explore how to optimize the function for faster execution or reduced memory usage, you can research advanced Python concepts like sets, iterators, and data structures, which can be extremely efficient for large lists or lists with a large number of duplicates.  This is particularly relevant for production code where performance and scalability are crucial.  However, for most applications, the simplicity and readability of the above code is a good starting point.