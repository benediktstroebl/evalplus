Here's the self-contained Python function that solves the problem of inserting a specified delimiter between every two consecutive elements in a list: 

```python
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:  # only insert delimit when even index
            result.append(delimiter)
        result.append(numbers[i])
    return result
``` 

This function takes a list of integers and a delimiter as input and returns a list where every other element is separated by the specified delimiter. 

Note that this function doesn't use any external modules and performs all the logic within the function, making it self-contained.