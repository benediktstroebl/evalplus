```python
def specialFilter(nums):
    oddFirst = [x for x in nums if int(str(x)[0]) % 2 == 1]
    oddLast = [x for x in nums if int(str(x)[-1]) % 2 == 1]
    return len(oddFirst & oddLast)
```

The script uses Python's abilities to work with strings and integers coherently to filter out numbers that follow the required criteria. It uses the semantically simple 'and' operator to find common elements in two odd-filtered number arrays, a lowercase 'and' is used for element intersection. The function outputs the number of elements that remain, which are numbers where both first and last digits are odd. 

The markdown code block below shows how you can test this function using a sample input and expected output:
```python
test_list = [15, -73, 14, -15, 33, -2, -3, 45, 21, 109]
expected_result = 1

result = specialFilter(test_list)

assert result == expected_result
```