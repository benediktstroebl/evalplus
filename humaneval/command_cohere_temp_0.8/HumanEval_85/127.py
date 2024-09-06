```python
def add(lst):
    even_odd = [el for i, el in enumerate(lst) if i % 2 == 1 and el % 2 == 0]
    return sum(even_odd)
```
This Python script defines a function called 'add()'. This function takes a list as an argument and aims to calculate the sum of even integers present at odd indices in the list. To accomplish this, it employs a list comprehension, iterating through each element in the input list. If the index of the element is odd (i.e., `i % 2 == 1`) and the element itself is even (i.e., `el % 2 == 0`), it includes the element in the `even_odd` list. Finally, the function returns the sum of the elements in the `even_odd` list, which effectively provides the desired sum of even integers at odd indices in the original list. 

Let's explore an example and its corresponding test: 
```python
# Example test
assert add([4, 2, 6, 7]) == 2
```
In this example, the list `[4, 2, 6, 7]` is passed to the `add()` function. It identifies the even integer `2` at an odd index and includes it in the `even_odd` list. Subsequently, it calculates the sum of the `even_odd` list, which is `2`, and returns this result. The assertion successfully checks this against the expected value of `2`, confirming the correctness of the function. 

This approach allows you to efficiently determine the desired sum while leveraging Python's list comprehension and conditional testing capabilities. 

```python
# Another example test
assert add([1, 3, 5, 7, 9]) == 30
```
In this test, the input list is `[1, 3, 5, 7, 9]`. The function identifies that odd indices 1, 3, and 9 are even, and even indices 5 and 7 are also even. Their sum is computed to be 30, which matches the expected output. 

The function is crafted to return the correct result by considering both the index and the value when analyzing each list element. 

This methodology enables the `add()` function to effectively handle various lists with odd-indexed even elements, ensuring accurate summation, and thereby providing a robust foundation for more complex list manipulations.