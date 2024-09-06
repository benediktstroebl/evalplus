```python
def compare(game, guess):
    result = [abs(x-y) if x != y else 0 for x,y in zip(game, guess)]
    return result
```

The solution works by using Python's zipper to iterate over each element in `game` and `guess` simultaneously. For each pair of elements, it calculates the absolute difference between them and assigns it to the corresponding index in `result` if they are different, or assigns 0 if the guess was correct. 

This approach ensures that the function works for any length of `game` and `guess` arrays and can be easily integrated into larger programs that may only require this function as opposed to standalone code blocks. 

To verify the functionality, you can uncomment the test code block and execute the script:
```python
# test = [([1,2,3,4,5,1],[1,2,3,4,2,-2]),([0,5,0,0,0,4],[4,1,1,0,0,-2])]
# print(compare(*test[0]))  # [0,0,0,0,3,3]
# print(compare(*test[1]))  # [4,4,1,0,0,6]
``` 
It will output:
```
[0, 0, 0, 0, 3, 3]
[4, 4, 1, 0, 0, 6]
``` 
Indicating that the function operates correctly.